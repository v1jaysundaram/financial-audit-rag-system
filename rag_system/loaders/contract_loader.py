# import necessary libraries
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# load contracts
file_path = r"D:\Data Science_ML\Projects\GenAI\financial-audit-rag-system\data\contracts" 

contract_loader = DirectoryLoader(
    path=file_path,
    glob ="**/*.pdf",
    loader_cls=PyPDFLoader,
    show_progress=True 
)

contract_docs = contract_loader.load()

# Clean the text content
def clean_text(text):
    return ' '.join(text.split())

contract_docs_cleaned = [
    {
        "page_content": clean_text(doc.page_content),  # Cleaned text content
        "metadata": doc.metadata  # Preserve metadata        
    }
    for doc in contract_docs
]

"""print(contract_docs_cleaned[2:4])

print(f"Number of documents loaded: {len(contract_docs_cleaned)}")"""