# import necessary libraries
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from .contract_prompt import contract_prompt

# define the function to format the retrieved documents
def format_docs(retrieved_docs):
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    return context_text

# define the function to create the contract chain
def contract_chain(retriever):
    prompt = contract_prompt()
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    parser = StrOutputParser()

    parallel_chain = RunnableParallel({
        'context': retriever | RunnableLambda(format_docs),
        'question': RunnablePassthrough()
    })

    chain = parallel_chain | prompt | llm | parser
    return chain
