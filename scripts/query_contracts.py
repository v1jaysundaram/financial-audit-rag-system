# import necessary libraries
from rag_system.contracts.contract_retriever import retrieve_contracts
from rag_system.contracts.contract_chains import contract_chain

# set the supplier name and query
supplier = "Hall Snyder and Rodriguez Ltd"
query = "When does the contract end?"

# retrieve the contracts
retriever = retrieve_contracts(supplier_filter=supplier)

# Get the chain and run the query
qa_chain = contract_chain(retriever)
answer = qa_chain.invoke(query)

print(answer)