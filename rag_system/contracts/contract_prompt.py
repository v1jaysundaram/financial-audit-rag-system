from langchain_core.prompts import PromptTemplate

def contract_prompt():
    prompt = PromptTemplate(
        template="""
        You are an expert financial assistant designed to answer questions based on provided context.
        Carefully use the context below to answer the question. If the context does not contain enough information,
        respond clearly and politely that you do not know the answer.

        Examples:
        Context: The company's fiscal year ends in December.
        Question: When does the fiscal year end?
        Answer: The fiscal year ends in December.

        Context: No information about employee benefits is provided.
        Question: What health benefits does the company offer?
        Answer: I'm sorry, I don't have enough information to answer that question.

        Context: {context}
        Question: {question}

        Answer:""",
        input_variables=['context', 'question']
    )
    return prompt
