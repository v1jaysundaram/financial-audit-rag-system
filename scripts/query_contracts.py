# scripts/query_contracts.py

from rag_system.contracts.contract_retriever import retrieve_contracts
from rag_system.contracts.contract_chains import contract_chain

# Setup retriever
supplier = "Hall Snyder and Rodriguez Ltd"
query = "When does the contract end?"

retriever = retrieve_contracts(supplier_filter=supplier)

# Get the chain and run the query
qa_chain = contract_chain(retriever)
answer = qa_chain.invoke(query)

print(answer)