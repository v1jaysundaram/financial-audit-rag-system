from rag_system.contracts.contract_retriever import retrieve_contracts
from rag_system.contracts.contract_chains import contract_chain
from langchain.memory import ConversationEntityMemory
from langchain_openai import ChatOpenAI

# Setup
supplier = "Hall Snyder and Rodriguez Ltd"
retriever = retrieve_contracts(supplier_filter=supplier)
qa_chain = contract_chain(retriever)

# Initialize memory and LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
memory = ConversationEntityMemory(llm=llm)

def run_with_memory(query: str):
    memory_vars = memory.load_memory_variables(inputs={"question": query})
    history = memory_vars.get("history", "")
    if isinstance(history, dict):
        history = str(history)
    
    augmented_question = f"{history}\n\n{query}" if history else query
    response = qa_chain.invoke(augmented_question)
    memory.save_context(inputs={"question": query}, outputs={"answer": response})
    return response

# Example usage
response1 = run_with_memory("When does the contract end?")
print("Answer 1:", response1)

response2 = run_with_memory("Is there a renewal clause?")
print("Answer 2:", response2)
