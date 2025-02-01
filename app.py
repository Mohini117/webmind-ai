import streamlit as st
import os
import requests
import time
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Function to load external CSS
def load_css():
    with open("style.css", "r") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Load the CSS styles
load_css()

# App Title
st.markdown("<h1 style='text-align: center; color: #ff7eb3;'>WebMind AI 🧠</h1>", unsafe_allow_html=True)

# Get URL input
url = st.text_input("🔗 Enter the URL of the website you want to scrape")
scrape_clicked = st.button("🚀 Scrape Website")

# Function to validate and process the URL
def validate_url(url):
    if not url:
        return None, "⚠️ Please enter a website URL."
    if not (url.startswith("http://") or url.startswith("https://")):
        return None, "⚠️ Invalid URL. Use 'http://' or 'https://'."
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return None, f"⚠️ Cannot access website (Status Code: {response.status_code})."
        return url, None
    except requests.exceptions.RequestException:
        return None, "⚠️ Could not reach the website. Check the URL and try again."

# Handle URL validation when the button is clicked
if scrape_clicked:
    valid_url, error_msg = validate_url(url)

    if error_msg:
        st.warning(error_msg)
    else:
        if "vector" not in st.session_state:
            st.session_state.embeddings = OllamaEmbeddings(model="Llama3-8b-8192")
            st.session_state.loader = WebBaseLoader(valid_url)
            st.session_state.docs = st.session_state.loader.load()

            st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:50])
            st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

        st.success("✅ Website successfully scraped!")

# Check if scraping has been performed before allowing user prompts
if "vectors" in st.session_state:
    llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

    prompt_template = ChatPromptTemplate.from_template(
        """
        Answer the questions based on the provided context only.
        Please provide the most accurate response based on the question.
        <context>
        {context}
        <context>
        Question: {input}
        """
    )
    document_chain = create_stuff_documents_chain(llm, prompt_template)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    # Get user query
    prompt = st.text_input("💬 Ask something about the website")
    get_answer_clicked = st.button("🤖 Get Answer")

    if prompt and get_answer_clicked:
        start = time.process_time()
        response = retrieval_chain.invoke({"input": prompt})
        st.write("⏳ Response Time:", time.process_time() - start)
        st.write(response["answer"])

        # Show relevant documents in expander
        with st.expander("📌 Similarity Search"):
            for i, doc in enumerate(response["context"]):
                st.write(doc.page_content)
                st.write("--------------------------------")
