from rag_system.contracts.contract_loader import load_contracts
import os
from dotenv import load_dotenv

load_dotenv()

def clean_text(text):
    return ' '.join(text.split())

def extract_supplier(metadata: dict) -> str | None:
    filename = metadata.get("source")
    if filename:
        base = os.path.basename(filename)
        name, _ = os.path.splitext(base)
        return name.replace("_", " ")
    return None

def process_contracts(contract_docs):

    contract_cleaned = [
        {
            "page_content": clean_text(doc.page_content),
            "metadata": doc.metadata
        }
        for doc in contract_docs
    ]

    contract_with_supplier = [
        {
            "page_content": doc["page_content"],
            "metadata": {
                **doc["metadata"],
                "supplier_name": extract_supplier(doc["metadata"])
            }
        }
        for doc in contract_cleaned
    ]

    return contract_with_supplier
