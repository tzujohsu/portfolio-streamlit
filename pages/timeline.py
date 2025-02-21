import streamlit as st
import os
import re
import json

from utils.retriever import Retriever
from utils.generator import HuggingfaceTimelineGenerator
from utils.document_loader import DocumentLoader
from streamlit_timeline import timeline



st.markdown("<h1 style='text-align: center; color: black;'>ChronoEvents: Timeline Generator</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="width: 60%; margin: 0 auto; text-align: center; font-size: 1.1rem;">
        <p>
        ChronoScope is an innovative LLM-powered tool that transforms news transcripts into offers structured, temporal insights. <br> <br>
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)
st.info("""Simply enter your topic or query in the input box below, and the tool will:
        1. Retrieve relevant information from the our RAG-Chorma database
        2. Generate a summarized timeline of events relevant to your input
        3. Display an interactive timeline visualization""", icon="ℹ️")


# Initialize necessary components
if "db" not in st.session_state:
    docloader = DocumentLoader()
    # docloader.load_documents_into_database()
    st.session_state["db"] = docloader.vector_store
    print("Database loaded successfully")
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Helper function to clear text
def clear_text():
    st.session_state.user_input = ""

retriever = Retriever(st.session_state["db"])
generator = HuggingfaceTimelineGenerator()

# Input section
with st.container():
    user_input = st.text_area("Enter your topic or query:", height=70, key="user_input")
    col1, col2 = st.columns([1,9])
    with col1:
        st.button("Clear Input", on_click=clear_text, type="secondary")
    with col2:
        generate_button = st.button("Generate Timeline", type="primary")

# Results section
if generate_button and user_input:
    with st.spinner("Generating timeline..."):
        # Retrieve relevant documents
        retrieved_df = retriever.get_similarity_search(user_input)
        
        # Generate timeline
        summarized_list = generator.get_summary(retrieved_df)
        timeline_data = generator.get_timeline_data(summarized_list, user_input)
        timeline_data_json = json.dumps(timeline_data)
        timeline(timeline_data_json, height=600)
