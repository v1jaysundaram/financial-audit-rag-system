# import necessary libraries
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def clean_text(text):
    """Remove extra whitespaces from text."""
    return ' '.join(text.split())

def load_contracts():
    """
    Loads all PDF contracts.

    Returns:
        List[Dict]: Cleaned documents with metadata.
    """

    file_path = r"D:\Data Science_ML\Projects\GenAI\financial-audit-rag-system\data\contracts" 

    contract_loader = DirectoryLoader(
        path=file_path,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True
    )

    contract_docs = contract_loader.load()

    contract_docs_cleaned = [
        {
            "page_content": clean_text(doc.page_content), # Cleaned text 
            "metadata": doc.metadata  # Preserve metadata
        }
        for doc in contract_docs
    ]

    return contract_docs_cleaned