import streamlit as st
from rag_system.contracts.contract_retriever import retrieve_contracts
from rag_system.contracts.contract_chains import contract_chain
from langchain.memory import ConversationEntityMemory
from langchain_openai import ChatOpenAI

# Initialize LLM and memory once globally (outside main)
if "llm" not in st.session_state:
    st.session_state.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

if "memory" not in st.session_state:
    st.session_state.memory = ConversationEntityMemory(
        llm=st.session_state.llm,
        return_messages=True
    )

# Track previous supplier to reset memory when supplier changes
if "prev_supplier" not in st.session_state:
    st.session_state.prev_supplier = ""

def main():
    st.title("Fin AI")
    st.caption("AI-driven insights across your contracts, invoices, and payments.")

    supplier = st.text_input("Supplier Name", help="Filter results by supplier")
    query = st.text_area("Query", help="Ask a question about the contract")

    # If supplier changed, clear the memory
    if supplier.strip() and supplier != st.session_state.prev_supplier:
        st.session_state.memory.clear()  # Clear conversation history
        st.session_state.prev_supplier = supplier

    if st.button("Get Answer"):
        if not supplier.strip():
            st.error("Please enter a supplier name.")
            return
        if not query.strip():
            st.error("Please enter a query.")
            return

        with st.spinner("Retrieving answer..."):
            try:
                # Set up retriever and QA chain for current supplier
                retriever = retrieve_contracts(supplier_filter=supplier)
                qa_chain = contract_chain(retriever)

                # Load memory variables (may include 'history' and entities)
                memory_vars = st.session_state.memory.load_memory_variables({"question": query})
                history = memory_vars.get("history", "")

                # Convert history to string if not already
                if not isinstance(history, str):
                    history = str(history)

                # Combine history and query to keep conversation context
                full_query = history + "\n\n" + query if history else query

                # Get answer from QA chain
                answer = qa_chain.invoke(full_query)

                # Save the new interaction in memory
                st.session_state.memory.save_context(
                    inputs={"question": query},
                    outputs={"answer": answer}
                )

                # Show answer to user
                st.markdown("### Answer:")
                st.write(answer)

            except Exception as e:
                st.error(f"Error during retrieval: {e}")

# Sidebar footer
st.sidebar.write("Built by [Vijay](https://www.linkedin.com/in/vijay-sundaram/)", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
