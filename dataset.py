"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    "wonderful",
    "fantastic",
    "thrilled",
    "joyful",
    "glad",
    "grateful",
    "blessed",
    "ecstatic",
    "delighted",
    "cheerful",
    "pumped",
    "stoked",
    "hyped",
    "winning",
    "vibing",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    "miserable",
    "frustrated",
    "depressed",
    "exhausted",
    "hopeless",
    "defeated",
    "overwhelmed",
    "dread",
    "worried",
    "disappointed",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "got a B on the exam, which is good... but I was really hoping for an A",
    "lowkey proud of myself for finishing that project, but I am completely drained",
    "just got the job offer!!! also terrified I am gonna mess it up",
    "laughed all night with friends and still felt weirdly lonely on the way home",
    "finally canceled plans and stayed in, and honestly it feels amazing",
    "trying to stay positive, but my brain keeps replaying every awkward thing I said",
    "I love getting stuck in traffic",
    # Added examples — more balanced across all four labels
    "this is the best day ever, no cap",
    "I am so grateful for everything right now",
    "highkey thrilled about the new semester",
    "woke up feeling wonderful and ready to go",
    "I passed my driving test!!!",
    "honestly just vibing today :)",
    "everything went wrong and I can not stop crying",
    "I am so frustrated I could scream",
    "failed the quiz and now I feel hopeless",
    "nothing is going right today :(",
    "just existing, not much going on",
    "another day, another dollar I guess",
    "got the promotion but now I am worried I will burn out",
    "really happy for my friend but lowkey jealous ngl",
    "the concert was amazing but my feet are destroyed",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    "mixed",     # "got a B on the exam, which is good... but I was really hoping for an A"
    "mixed",     # "lowkey proud of myself for finishing that project, but I am completely drained"
    "mixed",     # "just got the job offer!!! also terrified I am gonna mess it up"
    "mixed",     # "laughed all night with friends and still felt weirdly lonely on the way home"
    "positive",  # "finally canceled plans and stayed in, and honestly it feels amazing"
    "mixed",     # "trying to stay positive, but my brain keeps replaying every awkward thing I said"
    "negative",  # "I love getting stuck in traffic"
    # Added labels
    "positive",  # "this is the best day ever, no cap"
    "positive",  # "I am so grateful for everything right now"
    "positive",  # "highkey thrilled about the new semester"
    "positive",  # "woke up feeling wonderful and ready to go"
    "positive",  # "I passed my driving test!!!"
    "positive",  # "honestly just vibing today :)"
    "negative",  # "everything went wrong and I can not stop crying"
    "negative",  # "I am so frustrated I could scream"
    "negative",  # "failed the quiz and now I feel hopeless"
    "negative",  # "nothing is going right today :("
    "neutral",   # "just existing, not much going on"
    "neutral",   # "another day, another dollar I guess"
    "mixed",     # "got the promotion but now I am worried I will burn out"
    "mixed",     # "really happy for my friend but lowkey jealous ngl"
    "mixed",     # "the concert was amazing but my feet are destroyed"
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
