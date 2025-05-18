from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.retrievers import ContextualCompressionRetriever
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# define the function to retrieve contracts using FAISS
def retrieve_contracts(supplier_filter=None):
    embeddings = OpenAIEmbeddings()
    persist_path="embeddings/contracts"

    # Load the FAISS vectorstore
    vectorstore = FAISS.load_local(
    folder_path=persist_path,
    embeddings=embeddings,
    allow_dangerous_deserialization=True
    )   

    # Manually filter documents by partial metadata match
    if supplier_filter:
        supplier_filter = supplier_filter.lower()
        all_docs = list(vectorstore.docstore._dict.values())
        filtered_docs = [
            doc for doc in all_docs
            if supplier_filter in doc.metadata.get("supplier_name", "").lower()
        ]

        # If matches found, rebuild FAISS with filtered docs
        if filtered_docs:
            vectorstore = FAISS.from_documents(filtered_docs, embedding=embeddings)
        else:
            print(f"No contracts found for supplier filter: {supplier_filter}")
            return None  # or return empty retriever if you prefer

    # Set up retriever
    base_retriever = vectorstore.as_retriever()

    # Use GPT-based compression
    llm = ChatOpenAI(model='gpt-4')
    base_compressor = LLMChainExtractor.from_llm(llm)

    compressor_retriever = ContextualCompressionRetriever(
        base_retriever=base_retriever,
        base_compressor=base_compressor
    )

    return compressor_retriever