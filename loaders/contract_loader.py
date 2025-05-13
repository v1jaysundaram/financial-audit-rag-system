# import necessary libraries
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from dotenv import load_dotenv

file_path = r"D:\Data Science_ML\Projects\GenAI\financial-audit-rag-system\data\contracts" 
contract_loader = DirectoryLoader(
    path=file_path,
    glob ="**/*.pdf",
    loader_cls=PyPDFLoader,
    show_progress=True
)

contract_docs = contract_loader.load()

# Clean up text by removing excessive line breaks and extra spaces
def clean_text(text):
    return ' '.join(text.split())

# Clean each document's content while preserving metadata
contract_docs_cleaned = [
    {
        "metadata": doc.metadata,  # Preserve metadata
        "page_content": clean_text(doc.page_content)  # Cleaned text content
    }
    for doc in contract_docs
]

print(contract_docs_cleaned[0])  # Print the first cleaned document for verification