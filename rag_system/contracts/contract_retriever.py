# import necessary libraries
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.retrievers import ContextualCompressionRetriever
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# define the function to retrieve contracts
def retrieve_contracts(supplier_filter=None):
    
    contract_vectorstore = Chroma(
        embedding_function=OpenAIEmbeddings(),
        persist_directory="embeddings/contracts",
        collection_name="contracts"
    )

    # filter the vectorstore based on supplier name
    if supplier_filter:
        metadata_filter = {"supplier_name": supplier_filter}
        base_retriever = contract_vectorstore.as_retriever(search_kwargs={"filter": metadata_filter})
    else:
        base_retriever = contract_vectorstore.as_retriever()
    
    llm = ChatOpenAI(model='gpt-4')

    base_compressor = LLMChainExtractor.from_llm(llm) 

    compressor_retriever = ContextualCompressionRetriever(
        base_retriever=base_retriever,
        base_compressor=base_compressor
    )

    return compressor_retriever
