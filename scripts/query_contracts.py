from rag_system.contracts.contract_retriever import retrieve_contracts

contract_retriever = retrieve_contracts(supplier_filter="Hall Snyder and Rodriguez Ltd")
query = "What is the notice period for termination?"
results = contract_retriever.invoke(query)

for i, doc in enumerate(results, 1):
    print(f"\n📄 Result #{i}\n{'-'*40}")
    print(doc.page_content)  # print first 1000 characters only