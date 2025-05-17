from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def split_contracts(contract_docs: list[Document], chunk_size: int, chunk_overlap: int) -> list[Document]:
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunked_docs = []

    for doc in contract_docs:
        chunks = splitter.split_text(doc.page_content)
        chunked_docs.extend([
            Document(page_content=chunk, metadata=doc.metadata)
            for chunk in chunks
        ])

    return chunked_docs

