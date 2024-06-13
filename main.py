import streamlit as st
from utils import (
    upload_file,
)

with st.form("ai_admin"):
    st.header('Choose   _AIAgent_   🤖 parameters', divider='blue')

    llm = st.selectbox("LLM: ", ("OpenAI",))

    api_key = st.text_input("API Key: ")
    
    topk = st.number_input("Top K:", min_value=1, max_value=10)

    system_prompt = st.text_area("System prompt: ")

    pdf_doc = upload_file()

    submitted = st.form_submit_button("Create Agent")

    if submitted:
        st.write("LLM: ", llm,
                 "API Key: ", api_key,
                 "Top K: ", topk,
                 "System Prompt: ", system_prompt,
                 "Knowledge doc: ", pdf_doc)

