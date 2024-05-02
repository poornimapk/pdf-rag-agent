from dotenv import load_dotenv
import streamlit as st
from utils import (
    upload_file,
    chunk_pdf,
    create_documents_from_chunks,
    setup_vector_database_and_create_vector_index,
    chat_engine_response,
)
from core.constants import COLLECTION_NAME


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with PDF",
                       page_icon="📚")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with PDF 📚")
    # user_question = st.text_input("Ask a question from your PDF")

    with st.sidebar:
        st.subheader("Your document")
        path = upload_file()
        if st.button("Process"):
            with st.spinner("Processing"):
                #st.write(path)
                pages_and_chunks = chunk_pdf(path)
                documents = create_documents_from_chunks(pages_and_chunks)
                # st.write(documents)
                vector_index = setup_vector_database_and_create_vector_index(documents=documents,
                                                                             collection_name=COLLECTION_NAME)
                st.session_state.vector_index = vector_index
                # Delete temp file TODO
                st.write("PDF loaded to Vector store successfully!")

    # Create chat engine
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "agent", "content": "How may I help you?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    if st.session_state.messages[-1]["role"] != "agent":
        with st.chat_message("agent"):
            with st.spinner("Thinking ... "):
                response = chat_engine_response(index=st.session_state.vector_index, prompt_input=prompt)
                st.write(response)
        message = {"role": "agent", "content": response}
        st.session_state.messages.append(message)


if __name__ == '__main__':
    main()
