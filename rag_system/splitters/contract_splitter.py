from rag_system.loaders.contract_loader import load_contracts
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import re
import os

load_dotenv()

# Load contract docs
contract_docs = load_contracts()


def clean_text(text):
    """Remove extra whitespaces, tabs, and newlines from text."""
    return ' '.join(text.split())

# Clean the contract documents
contract_cleaned = [
    {
        "page_content": clean_text(doc.page_content),  # Cleaned text
        "metadata": doc.metadata  # Preserve metadata
    }
    for doc in contract_docs
]

def extract_filename_as_supplier(metadata: dict) -> str | None:
    """
    Extract supplier name from the filename stored in the metadata.
    Assumes the file name represents the supplier name (e.g., Hall_Snyder_Ltd.pdf).
    """
    filename = metadata.get("source")  # or "file_path" depending on your loader
    if filename:
        base = os.path.basename(filename)
        name, _ = os.path.splitext(base)
        return name.replace("_", " ")
    return None


# Process contracts and add supplier name based on file path
contract_final = [
    {
        "page_content": doc["page_content"],
        "metadata": {
            **doc["metadata"],
            "supplier_name": extract_filename_as_supplier(doc["metadata"])
        }
    }
    for doc in contract_cleaned
]


def split_contract_into_chunks(contract_final):
    """
    Split the contract text into chunks and add metadata.

    Parameters:
        contract_final (list): List of contract documents with metadata.

    Returns:
        list: List of dictionaries containing chunks with their respective metadata.
    """
    chunks_with_metadata_all = []
    
    for contract_doc in contract_final:
        # Initialize the text splitter
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=200,
            chunk_overlap=20,
            length_function=len
        )

        # Split the contract text into chunks
        chunks = text_splitter.split_text(contract_doc['page_content'])

        # Combine chunks with metadata
        chunks_with_metadata = [
            {"chunk": chunk, "metadata": contract_doc['metadata']}
            for chunk in chunks
        ]

        # Append to the result list
        chunks_with_metadata_all.extend(chunks_with_metadata)
    
    return chunks_with_metadata_all

# Now you can call this function to get the chunks
chunks_with_metadata = split_contract_into_chunks(contract_final)

# Print the first 2 chunks as an example
print(chunks_with_metadata[:3])

