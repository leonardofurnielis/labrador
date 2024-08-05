from typing import List

class CharacterTextSplitter:

    def __init__(self,
                 chunk_size: int = 512,
                 chunk_overlap: int = 256,
                 separator=["\n\n", " "]) -> None:

        if chunk_overlap > chunk_size:
            raise ValueError(
                f"Got a larger `chunk_overlap` ({chunk_overlap}) than `chunk_size` "
                f"({chunk_size}). `chunk_overlap` should be smaller."
            )

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap