import streamlit as st
import pandas as pd
import time
from agent import ask_bank

st.set_page_config(
    page_title="BankQuery AI",
    page_icon="🏦",
    layout="centered"
)

# Header
st.title("🏦 BankQuery AI")
st.caption("Ask questions about banking data in plain English — powered by Gemini AI")

# Sidebar
with st.sidebar:
    st.header("💡 Try These Questions")
    st.markdown("Click any question below to run it instantly")

    examples = [
        "How many customers do we have?",
        "What is the average transaction amount?",
        "Show top 5 customers by total spending",
        "How many male vs female customers do we have?",
        "What is the most popular payment type?",
        "Show customers with credit score above 750",
        "Which location has the highest number of customers?",
        "What is the average credit limit by occupation?",
        "Show total spending by product category",
        "Which customers have the highest credit utilisation?"
    ]

    for example in examples:
        if st.button(example, use_container_width=True):
            st.session_state.selected_question = example

    st.divider()
    st.markdown("**About this project**")
    st.markdown("Built on real bank credit card data with 1000 customers and transactions")
    st.markdown("Powered by Google Gemini AI + MySQL")

# Chat history initialise
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "dataframe" in message:
            st.dataframe(message["dataframe"], use_container_width=True)

# Handle sidebar button click
if "selected_question" in st.session_state:
    question = st.session_state.pop("selected_question")

    with st.chat_message("user"):
        st.markdown(question)
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("assistant"):
        with st.spinner("Gemini is thinking..."):
            time.sleep(2)
            cols, rows, sql = ask_bank(question)

        if cols:
            df = pd.DataFrame(rows, columns=cols)
            response = f"✅ Found **{len(rows)}** result(s)\n\n**SQL Generated:**\n```sql\n{sql}\n```"
            st.markdown(response)
            st.dataframe(df, use_container_width=True)
            st.session_state.messages.append({
                "role": "assistant",
                "content": response,
                "dataframe": df
            })
        else:
            error_msg = f"❌ {sql}"
            st.error(error_msg)
            st.session_state.messages.append({
                "role": "assistant",
                "content": error_msg
            })
    st.rerun()

# Chat input box at bottom
if question := st.chat_input("Ask anything about your banking data..."):

    with st.chat_message("user"):
        st.markdown(question)
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("assistant"):
        with st.spinner("Gemini is thinking..."):
            cols, rows, sql = ask_bank(question)

        if cols:
            df = pd.DataFrame(rows, columns=cols)
            response = f"✅ Found **{len(rows)}** result(s)\n\n**SQL Generated:**\n```sql\n{sql}\n```"
            st.markdown(response)
            st.dataframe(df, use_container_width=True)
            st.session_state.messages.append({
                "role": "assistant",
                "content": response,
                "dataframe": df
            })
        else:
            error_msg = f"❌ {sql}"
            st.error(error_msg)
            st.session_state.messages.append({
                "role": "assistant",
                "content": error_msg
            })