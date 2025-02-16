import streamlit as st
import streamlit.components.v1 as components
import requests
from bs4 import BeautifulSoup
import random


st.markdown("""
    <h1 style='text-align: center; margin-bottom: 2rem;'>News Categorization Tool</h1>
    """, unsafe_allow_html=True)


def get_categorization(text: str):
    url = "http://18.205.115.194/categorize"
    params = {"txt": text}
    
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()  # Raise error for HTTP issues
        return response.json()  # Assuming FastAPI returns JSON
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Function to fetch a random CNN Lite article
def get_random_cnn_article():
    base_url = "https://lite.cnn.com/"
    response = requests.get(base_url)
    
    if response.status_code != 200:
        return "Failed to fetch articles."

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract article links
    articles = [a["href"] for a in soup.find_all("a", href=True) if a["href"].startswith("/")]
    if not articles:
        return "No articles found."
    
    # Pick a random article
    random_article = random.choice(articles)
    article_url = f"{base_url}{random_article}"
    
    # Fetch article content
    response = requests.get(article_url)
    if response.status_code != 200:
        return "Failed to fetch the article."

    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = [p.get_text() for p in soup.find_all("p")]
    txt = "".join(paragraphs).split('See Full Web Article')[0]
    txt = txt.strip()
    return txt, article_url


if "text_input" not in st.session_state:
    st.session_state.text_input = ""

# Create main columns with better proportions
col1, col2 = st.columns([3, 4])

with col1:
    st.markdown("### Input Text")
    # Text area with better sizing
    text_input = st.text_area(
        label="Enter text for classification",
        value=st.session_state.text_input,
        height=250,
        placeholder="Paste your text here or use the buttons below to get a sample..."
    )
    
    # Create two columns for buttons
    button_col1, button_col2 = st.columns(2)
    
    with button_col1:
        if st.button("🔄 Random CNN Article", use_container_width=True):
            st.session_state.text_input, st.session_state.cnn_url = get_random_cnn_article()
            st.rerun()
    
    with button_col2:
        if st.button("🗑️ Clear Text", use_container_width=True):
            st.session_state.text_input = ""
            st.session_state.cnn_url = ""  # Clear the URL as well
            st.rerun()
    
    # Display CNN URL if it exists
    if hasattr(st.session_state, 'cnn_url') and st.session_state.cnn_url:
        st.markdown(
            f"""<div style='margin-top: 0.5rem; padding: 0.5rem; background-color: #e8f4f9; border-radius: 0.5rem;'>
            📰 <b>Source:</b> <a href="{st.session_state.cnn_url}" target="_blank">{st.session_state.cnn_url}</a>
            </div>""",
            unsafe_allow_html=True
        )
    
    # Add a helpful note
    st.markdown("""
        <div style='margin-top: 1rem; padding: 1rem; background-color: #f0f2f6; border-radius: 0.5rem;'>
        💡 <i>Tip: You can get a sample article using the "Random CNN Article" button or paste your own text.</i>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### Categorization Results")
    # Add some spacing before the classify button
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🔍 Classify Text", type="primary", use_container_width=True):
        if text_input:
            with st.spinner("Analyzing text..."):
                result = get_categorization(text_input)
                # Display results in a more structured way
                st.success("Classification complete!")
                st.json(result)
        else:
            st.error("⚠️ Please enter some text to categorize!")
    