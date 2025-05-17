from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_contracts(contract_docs, chunk_size, chunk_overlap):
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunked_docs = []

    for doc in contract_docs:
        chunks = splitter.split_text(doc["page_content"])
        chunked_docs.extend([
            {"page_content": chunk, "metadata": doc["metadata"]}
            for chunk in chunks
        ])

    return chunked_docs
