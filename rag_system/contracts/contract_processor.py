from rag_system.contracts.contract_loader import load_contracts
import os
from dotenv import load_dotenv
from langchain_core.documents import Document

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

def process_contracts(contract_docs: list[Document]) -> list[Document]:
    processed_docs = []
    for doc in contract_docs:
        cleaned_text = clean_text(doc.page_content)
        supplier = extract_supplier(doc.metadata)
        updated_metadata = dict(doc.metadata)
        if supplier:
            updated_metadata["supplier_name"] = supplier
        processed_docs.append(
            Document(page_content=cleaned_text, metadata=updated_metadata)
        )
    return processed_docs
