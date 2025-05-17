from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

persist_dir = "contracts"  # same as in embed_contracts persist_directory

if __name__ == "__main__":
    # Load existing vectorstore
    contract_vectorstore = Chroma(
        embedding_function=OpenAIEmbeddings(),
        persist_directory=persist_dir,
        collection_name="contracts",
    )

