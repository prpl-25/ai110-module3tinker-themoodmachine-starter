# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

import re
from typing import List, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

        # Extra vocabulary that appears often in informal posts.
        self.positive_words.update({"nice", "proud", "hopeful", "wholesome", "sick"})
        self.negative_words.update({"terrified", "lonely", "drained", "awkward", "anxious"})

        # Heavier weights for stronger sentiment words.
        self.positive_weights = {
          "love": 2,
          "amazing": 2,
          "awesome": 2,
          "great": 2,
          "sick": 2,
        }
        self.negative_weights = {
          "hate": 2,
          "terrible": 2,
          "awful": 2,
          "terrified": 2,
          "stressed": 2,
        }

        self.negators = {"not", "no", "never", "hardly"}
        self.intensifiers = {"very", "really", "so", "super", "extremely", "highkey"}
        self.contrast_words = {"but", "however", "though"}

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        TODO: Improve this method.

        Right now, it does the minimum:
          - Strips leading and trailing whitespace
          - Converts everything to lowercase
          - Splits on spaces

        Ideas to improve:
          - Remove punctuation
          - Handle simple emojis separately (":)", ":-(", "🥲", "😂")
          - Normalize repeated characters ("soooo" -> "soo")
        """
        cleaned = text.strip().lower()
        # Keep alphabetic tokens and drop punctuation for stable matching.
        tokens = re.findall(r"[a-z]+(?:'[a-z]+)?", cleaned)

        return tokens

    def _analyze_tokens(self, tokens: List[str]) -> Tuple[int, List[str], List[str]]:
        """
        Analyze tokens and return:
          (score, positive_hits, negative_hits)

        Includes simple one-word negation handling:
          - "not happy" counts as negative
          - "not bad" counts as positive
        """
        score = 0
        positive_hits: List[str] = []
        negative_hits: List[str] = []

        # If a sentence has contrast ("..., but ..."), later clause often
        # carries the final sentiment more strongly.
        contrast_idx = -1
        for idx, token in enumerate(tokens):
          if token in self.contrast_words:
            contrast_idx = idx

        i = 0
        negate_next = 0
        boost_next = 1
        while i < len(tokens):
          token = tokens[i]

          if token in self.contrast_words:
            i += 1
            continue

          if token in self.negators:
            negate_next = 2
            i += 1
            continue

          if token in self.intensifiers:
            boost_next = 2
            i += 1
            continue

          token_score = 0

          # "sick" can be slang-positive, but in "feel sick" it is negative.
          if token == "sick":
            prev_token = tokens[i - 1] if i > 0 else ""
            if prev_token in {"feel", "feeling", "felt", "am", "is", "was"}:
              token_score = -2
            else:
              token_score = 2
          elif token in self.positive_words:
            token_score = self.positive_weights.get(token, 1)
          elif token in self.negative_words:
            token_score = -self.negative_weights.get(token, 1)

          if token_score != 0:
            if negate_next > 0:
              token_score *= -1
              negate_next = 0

            token_score *= boost_next
            boost_next = 1

            if contrast_idx != -1 and i > contrast_idx:
              token_score *= 2

            score += token_score

            if token_score > 0:
              positive_hits.append(token)
            else:
              negative_hits.append(token)
          else:
            # Reset stale intensifier if no sentiment token follows quickly.
            boost_next = 1

          if negate_next > 0:
            negate_next -= 1

          i += 1

        return score, positive_hits, negative_hits

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score" for the given text.

        Positive words increase the score.
        Negative words decrease the score.

        TODO: You must choose AT LEAST ONE modeling improvement to implement.
        For example:
          - Handle simple negation such as "not happy" or "not bad"
          - Count how many times each word appears instead of just presence
          - Give some words higher weights than others (for example "hate" < "annoyed")
          - Treat emojis or slang (":)", "lol", "💀") as strong signals
        """
        tokens = self.preprocess(text)
        score, _, _ = self._analyze_tokens(tokens)
        return score

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        The default mapping is:
          - score > 0  -> "positive"
          - score < 0  -> "negative"
          - score == 0 -> "neutral"

        TODO: You can adjust this mapping if it makes sense for your model.
        For example:
          - Use different thresholds (for example score >= 2 to be "positive")
          - Add a "mixed" label for scores close to zero
        Just remember that whatever labels you return should match the labels
        you use in TRUE_LABELS in dataset.py if you care about accuracy.
        """
        tokens = self.preprocess(text)
        score, positive_hits, negative_hits = self._analyze_tokens(tokens)

        # Use "mixed" only when both signals exist and net sentiment is weak.
        if positive_hits and negative_hits and abs(score) <= 1:
          return "mixed"
        if score > 0:
          return "positive"
        if score < 0:
          return "negative"
        return "neutral"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        tokens = self.preprocess(text)
        score, positive_hits, negative_hits = self._analyze_tokens(tokens)

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
