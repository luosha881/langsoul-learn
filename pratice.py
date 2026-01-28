from importlib.resources import contents
from typing import List
def split_my_document(text: str, chunk_size: int = 1000, overlap: int = 200) -> list:
    """
    Splits the input text into chunks of specified size with a given overlap.

    Parameters:
    text (str): The input text to be split.
    chunk_size (int): The size of each chunk. Default is 1000 characters.
    overlap (int): The number of overlapping characters between chunks. Default is 200 characters.

    Returns:
    list: A list of text chunks.
    """
    chunks = []
    start = 0
    text_length = len(text)
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap")
    if not text:
        return chunks
    if chunk_size <= 0 or overlap < 0:
        raise ValueError("chunk_size must be positive and overlap must be non-negative")
    def find_nearest_punctuation(text: str, start: int, end: int) -> int:
        punctuation_marks = {'.', '!', '?', ',', ';', ':'}
        for i in range(end-1, max(end - 30, 0), -1):
            if i < len(text) and text[i] in punctuation_marks:
                return i + 1  # Include the punctuation mark
        return end  # No punctuation found, return original end

    while start < text_length:
        end = min(start + chunk_size, text_length)
        end = find_nearest_punctuation(text, start, end)
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks
# Example usage
if __name__ == "__main__":
    sample_text = ("This is a sample document. It contains multiple sentences! "
                   "The purpose is to demonstrate the splitting function? "
                   "Let's see how it works, shall we: by splitting text into chunks."
                   * 5)  # Repeat to create a longer text
    result = split_my_document(sample_text, chunk_size=100, overlap=10)
    for i, chunk in enumerate(result):
        print(f"Chunk {i+1}:\n{chunk}\n")
    