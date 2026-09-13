import re


def preprocess_text(text: str) -> str:
    # Convert text to lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()

# re.sub(
#     pattern,       ← what should I find?
#     replacement,   ← what should I replace it with?
#     text           ← where should I search?
# )
# \s means whitespace characters.
# ^ means NOT.
# r at beginning is raw string literal, so backslashes are treated literally.

