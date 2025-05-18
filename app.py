
import streamlit as st
from rag_system.contracts.contract_retriever import retrieve_contracts
from rag_system.contracts.contract_chains import contract_chain

def main():
    st.title("Fin AI")
    st.caption("AI-driven insights across your contracts, invoices, and payments.")
    
    supplier = st.text_input("Supplier Name", help="Filter results by supplier")
    query = st.text_area("Query", help="Ask a question about the contract")
    
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

# Sidebar footer
st.sidebar.write("Built by [Vijay](https://www.linkedin.com/in/vijay-sundaram/)", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
