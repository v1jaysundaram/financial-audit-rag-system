# import necessary libraries
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# define the function to embed contracts
def embed_contracts(docs):
    vectorstore = Chroma(
        embedding_function=OpenAIEmbeddings(),
        persist_directory="embeddings/contracts",
        collection_name="contracts"
    )
    vectorstore.add_documents(docs)
    vectorstore.persist()
    return vectorstore
