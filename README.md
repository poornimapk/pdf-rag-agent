# Introduction
You can chat with a PDF agent which analyzes the PDF and answers any question from PDF.

# How it works
The RAG agent follows these steps to get your answers:
1. Load the PDF and extract it's contents.
2. Chunk the extracted contents semantically.
3. Currently, it chooses OpenAI as Language Model (Future it will support local LLMs)
4. It retrieves the contents with semantically similar items.
5. Generates response using LLM by feeding the semantically similar items as context.

# Dependencies
1. Install the dependent modules using requirements.txt
2. Add OpenAI API key to .env file

# How to run app
1. Run application by giving following command
``` 
streamlit run 1_🏠_Home.py
```