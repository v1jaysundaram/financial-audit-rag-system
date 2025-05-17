from rag_system.contracts.contract_loader import load_contracts
from rag_system.contracts.contract_processor import process_contracts
from rag_system.contracts.contract_splitter import split_contracts
from rag_system.contracts.contract_embeddings import embed_contracts

file_path = r"D:\Data Science_ML\Projects\GenAI\financial-audit-rag-system\data\contracts" 

if __name__ == "__main__":
    raw_contracts = load_contracts(file_path)
    cleaned_contracts = process_contracts(raw_contracts)
    chunked_contracts = split_contracts(cleaned_contracts, chunk_size=1000, chunk_overlap=200)
    contract_vectorstore = embed_contracts(chunked_contracts)

    print("Contracts processed and embedded successfully.")

    print(contract_vectorstore.get(include=["embedding", "documents", "metadatas"])[0])