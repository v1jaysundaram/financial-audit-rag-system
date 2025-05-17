import sys
from rag_system.contracts.contract_loader import load_contracts
from rag_system.contracts.contract_processor import process_contracts
from rag_system.contracts.contract_splitter import split_contracts
from rag_system.contracts.contract_embeddings import embed_contracts

def build_contracts():  

    file_path = r"D:\Data Science_ML\Projects\GenAI\financial-audit-rag-system\data\contracts"

    raw_contracts = load_contracts(file_path)
    cleaned_contracts = process_contracts(raw_contracts)
    chunked_contracts = split_contracts(cleaned_contracts, chunk_size=1000, chunk_overlap=200)
    contract_vectorstore = embed_contracts(chunked_contracts)

    print("Contracts processed and embedded successfully.")



if __name__ == "__main__":
    doc_type = sys.argv[1].lower() if len(sys.argv) > 1 else ""

    if doc_type == "contracts":
        build_contracts()
    elif doc_type == "invoices":
        build_invoices()
    elif doc_type == "payments":
        build_payments()
    else:
        print("Invalid input! Use: contracts, invoices, or payments.")
        sys.exit(1)



"""
python build_vectorstores.py contracts
python build_vectorstores.py invoices
python build_vectorstores.py payments

python -m scripts.build_vectorstores contracts
"""