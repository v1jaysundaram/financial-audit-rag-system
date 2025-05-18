# import necessary libraries
from langchain_openai import OpenAIEmbeddings
#from langchain.vectorstores import Chroma
from langchain_community.vectorstores import FAISS


"""# define the function to embed contracts
def embed_contracts(docs):
    vectorstore = Chroma(
        embedding_function=OpenAIEmbeddings(),
        persist_directory="embeddings/contracts",
        collection_name="contracts"
    )
    vectorstore.add_documents(docs)
    vectorstore.persist()
    return vectorstore

"""

# define the function to embed and persist contracts using FAISS
def embed_contracts(docs):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(
        docs, 
        embedding=embeddings
        )
    vectorstore.save_local("embeddings/contracts")
    return vectorstore

