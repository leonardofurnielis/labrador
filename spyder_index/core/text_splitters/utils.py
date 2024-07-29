from typing import List, Callable


def tokenizer(text: str) -> List:
    try:
        import tiktoken
    except ImportError:
        raise ImportError("tiktoken package not found, please install it with `pip install tiktoken`")

    enc = tiktoken.get_encoding("o200k_base")
    return enc.encode(text)


def split_by_sep(sep) -> Callable[[str], List[str]]:
    """Split text by separator."""
    return lambda text: text.split(sep)


def split_by_regex(regex: str) -> Callable[[str], List[str]]:
    """Split text by regex."""
    import re

    return lambda text: re.findall(regex, text)


def split_by_char() -> Callable[[str], List[str]]:
    """Split text by character."""
    return lambda text: list(text)


def split_by_sentence_tokenizer() -> Callable[[str], List[str]]:
    try:
        import nltk
    except ImportError:
        raise ImportError("nltk package not found, please install it with `pip install nltk`")

    _tokenizer = nltk.tokenize.PunktSentenceTokenizer()
    return lambda text: _tokenizer.sentences_from_text(text)
