import sys
from unstructured.partition.pdf import partition_pdf
from core.exception import CustomException
from core.logger import logging


class Chunker:
    def __init__(self,file_path:str):
        self.file_path = file_path
    
    def chunk(self):
        try:
            logging.info(f"Chunking PDF file: {self.file_path}")
            chunks = partition_pdf(
                filename= self.file_path, # Path to the PDF file
                infer_table_structure=True, # Automatically detect table structure
                strategy="hi_res", # Use high-resolution strategy for better accuracy

                extract_image_block_types=["Image"], # Extract images as blocks

                extract_image_block_to_payload=True, # Include images in the payload

                chunking_strategy="by_title", # Chunk by title for better organization
                max_characters=10000, # Set maximum characters per chunk
                combine_text_under_n_chars=2000, # Combine text under 2000 characters
                new_after_n_chars = 6000, # Start a new chunk after 6000 characters
        
            )
            logging.info(f"Chunking completed. Number of chunks created: {len(chunks)}")
            return chunks
        except Exception as e:
            raise CustomException(e, sys)
        