# import necessary libraries
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# define the function to load contracts
def load_contracts():

    file_path = r"D:\Data Science_ML\Projects\GenAI\financial-audit-rag-system\data\contracts"

    contract_loader = DirectoryLoader(
        path=file_path,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True
    )

    contract_docs = contract_loader.load()

    return contract_docs