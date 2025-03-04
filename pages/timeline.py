import streamlit as st
from streamlit.components.v1 import html
import os
import re
import json
import random

from utils.retriever import Retriever
from utils.generator import HuggingfaceTimelineGenerator
from utils.document_loader import DocumentLoader
from utils.components import timeline_css, generate_timeline_html
from streamlit_timeline import timeline

# Initialize necessary components
if "db" not in st.session_state:
    docloader = DocumentLoader()
    # paths = os.listdir('data/data-news')
    # documents = docloader.load_documents_from_path(paths)
    # docloader.load_documents_into_database(documents)
    st.session_state["db"] = docloader.vector_store
    print("Database loaded successfully")
    min_date, max_date = docloader.get_database_dates()


st.markdown("""
<style>
.highlight {
    background-color: rgba(0,80,142,0.15);
    padding: 0 0.4rem;
    border-radius: 0.25rem;
    font-weight: bold;
    line-height: 1.5;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;'>ChronoEvents: Timeline Generator</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="width: 60%; margin: 0 auto; text-align: center; font-size: 1.1rem;">
        <h6>
        An innovative LLM/RAG-powered tool that transforms news transcripts into structured, temporal insights.
        </h6>
    </div>
    """, 
    unsafe_allow_html=True
)

st.markdown(f"<h6 style='text-align: center; color: grey;'>Data Source: CNN News Central ({min_date} - {max_date})</h6>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="width: 60%; margin: 0 auto; text-align: center; font-size: 1rem;">
        <br>
        <p>
        Simply enter your topic in the input box below, and the tool will: <br>
        1. Retrieve relevant information from the <span class='highlight'> LangChain Chroma </span> database <br>
        2. Generate a summarization of all the retrieved events with <span class='highlight'> Mistral-7b </span> <br>
        3. Display a timeline visualization for each date and event description <br>
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)
    
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Helper function to clear text
def clear_text():
    st.session_state.user_input = ""

# Helper function to generate display sample
sample_inputs = ['LA wildfire', 'chatgpt', 'plane crashes', 'super bowl', 'Artificial Intelligence']
def generate_random_sample():
    random_sample = random.choice(sample_inputs)
    st.session_state.user_input = random_sample

retriever = Retriever(st.session_state["db"])
generator = HuggingfaceTimelineGenerator()

def st_normal():
    _, col, _ = st.columns([1, 3, 1])
    return col

# Input section
with st_normal():
    # Input area with placeholder text
    user_input = st.text_area(
        "Enter your topic or query:",
        placeholder="Describe the topic or events you'd like to create a timeline for...",
        height=70,
        key="user_input"
            )

    col1, col2, col3 = st.columns([4, 1, 1])

    with col1:
        # Generate Random Sample button
        st.button("Random topics", on_click=generate_random_sample, type="secondary")

    with col2:
        # Clear Input button
        st.button("Clear Input", on_click=clear_text, type="secondary")

    with col3:
        # Generate timeline button
        generate_button = st.button("Generate", type="primary")

    # Results section
    if generate_button and user_input:
        with st.spinner("Generating timeline..."):
            # Retrieve relevant documents
            retrieved_df = retriever.get_similarity_search(user_input)
            
            # Generate timeline
            summarized_list = generator.get_summary(retrieved_df)
            timeline_data = generator.get_timeline_data(summarized_list, user_input)
            # timeline_data_json = json.dumps(timeline_data)
            # timeline(timeline_data_json, height=600)

            char_sum = 0
            for event in timeline_data:
                _, description = event['title'], event['description']
                char_sum += len(description)
            
            html(generate_timeline_html(timeline_data), height=320*char_sum//500+400)  # Increased height for better scrolling 
