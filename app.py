
import streamlit as st
from rag_system.contracts.contract_retriever import retrieve_contracts
from rag_system.contracts.contract_chains import contract_chain

def main():
    st.title("Financial Audit RAG System — Contracts Module")
    
    supplier = st.text_input("Supplier Name", help="Enter the supplier to filter contracts")
    query = st.text_area("Query", help="Enter your question about the contract")
    
    if st.button("Get Answer"):
        if not supplier.strip():
            st.error("Please enter a supplier name.")
            return
        if not query.strip():
            st.error("Please enter a query.")
            return
        
        with st.spinner("Retrieving answer..."):
            try:
                retriever = retrieve_contracts(supplier_filter=supplier)
                qa_chain = contract_chain(retriever)
                answer = qa_chain.invoke(query)
                st.markdown("### Answer:")
                st.write(answer)
            except Exception as e:
                st.error(f"Error during retrieval: {e}")

if __name__ == "__main__":
    main()
