from typing import List


def tokenizer(text: str) -> List:
    try:
        import tiktoken
    except ImportError:
        raise ImportError("tiktoken package not found, please install it with `pip install tiktoken`")

    enc = tiktoken.get_encoding("o200k_base")
    return enc.encode(text)


def num_tokens(text: str) -> int:
    return len(tokenizer(text))


def split_by_sep(text: str, sep) -> List[str]:
    """Split text by separator."""
    return text.split(sep)


def split_by_regex(text: str, regex: str) -> List[str]:
    """Split text by regex."""
    import re

    return re.findall(regex, text)


def split_by_char(text: str) -> List[str]:
    """Split text by character."""
    return list(text)


def split_by_sentence_tokenizer(text: str) -> List[str]:
    try:
        import nltk
    except ImportError:
        raise ImportError("nltk package not found, please install it with `pip install nltk`")

    _tokenizer = nltk.tokenize.PunktSentenceTokenizer()
    return _tokenizer.sentences_from_text(text)
