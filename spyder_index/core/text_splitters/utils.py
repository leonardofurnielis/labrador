def tokenizer(text):

    try:
        import tiktoken
    except ImportError:
        raise ImportError("tiktoken package not found, please install it with `pip install tiktoken`")

    enc = tiktoken.get_encoding("o200k_base")
    return enc.encode(text)


def num_tokens(text):
    return len(tokenizer(text))
