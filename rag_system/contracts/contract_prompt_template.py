from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    template="""
      You are an expert financial assistant for question-answering tasks.
      Use the following pieces of retrieved context to answer the question. 
      If you don't know the answer, just say that you don't know. 
      Keep the answer concise.

      Context: {context}
      Question: {question} 
 
    """,
    input_variables = ['context', 'question']
)