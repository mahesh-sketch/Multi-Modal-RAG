import sys
import os
from core.exception import CustomException
from core.logger import logging
from utils.chunker import Chunker


class ChunkSeparator:
    """Class to separate chunks from a
    PDF file into text and table and Image chunks."""
    def __init__(self):
        logging.info("Initializing ChunkSeparator.")
        pass
    
    def separate_chunks(self, chunks):
        try:
            logging.info("Separating chunks into text and tables.")

            text_chunks = []
            table_chunks = []

            for chunk in chunks:
                if "Table" in str(type(chunk)):
                    table_chunks.append(chunk)
                if "CompositeElement" in str(type((chunk))):
                    text_chunks.append(chunk)
            
            
            logging.info(f"Separated {len(text_chunks)} text chunks and {len(table_chunks)} table chunks.")
            
            return text_chunks, table_chunks
        except Exception as e:
            raise CustomException(e, sys)

    def separate_image_chunks(self, chunks):
        try:
            logging.info("Separating image chunks.")

            images_b64 = []
            for chunk in chunks:
                if "CompositeElement" in str(type(chunk)):
                    chunk_els = chunk.metadata.orig_elements
                    for el in chunk_els:
                        if "Image" in str(type(el)):
                            images_b64.append(el.metadata.image_base64)
            return images_b64
        except Exception as e:
            raise CustomException(e, sys)


""" if __name__ == "__main__":
    file_path = os.path.join(os.getcwd(), "UNION BUDGET 2025-26.pdf")
    chunk = Chunker(file_path=file_path).chunk()
    text_chunks, table_chunks = ChunkSeparator().separate_chunks(chunk)
    image_chunks = ChunkSeparator().separate_image_chunks(chunk)
    print(f"Text Chunks: {len(text_chunks)}")
    print(f"Table Chunks: {len(table_chunks)}")
    print(f"Image Chunks: {len(image_chunks)}")

    print(f"Text Chunk Example: {text_chunks[0] if text_chunks else 'No text chunks found.'}")
    print(f"Image Chunk Example: {image_chunks[0] if image_chunks else 'No image chunks found.'}")
 """