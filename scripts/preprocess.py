""" Preprocess function """
import string
import re


def preprocess(text: str, title: str):
    """

    Parameters
    ----------
    text: str :
        Reviewed text to be processed

    title: str :
        Reviewed title to be processed

    Returns
    -------
    processed: str :
        Concatened and cleaned text
    """
    processed = text + " " + title

    # Remove punctuation
    translation_table = str.maketrans("", "", string.punctuation)
    processed = processed.translate(translation_table)

    # Lower the string
    processed = processed.lower()

    #
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE,
    )
    processed = emoji_pattern.sub(r"", processed)

    return processed
