import streamlit as st
from css import css
from projects import *
from utils.components import *

# Apply CSS
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;'>Tzu-Jo Hsu's Portfolio</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <br>
    <div style="text-align: center;">
        <a href="https://www.linkedin.com/in/jocelyn-hsu-78518828b/" target="_blank">
            <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge" />
        </a>
        <a href="mailto:jocelynhsu.tjh@gmail.com" target="_blank">
            <img src="https://img.shields.io/badge/Email-0078D4?style=for-the-badge&logo=gmail&logoColor=white" alt="Email Badge" />
        </a>
        <a href="https://github.com/tzujohsu" target="_blank">
            <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Badge" />
        </a>
    </div>
    <br>
    """, 
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="width: 75%; margin: 0 auto; text-align: center; font-size: 1.2rem;">
        <p>Hi, I'm <strong>Tzu-Jo Hsu</strong>, I also go by Jocelyn.
        I'm passionate about data science and analytics.<br>
        I build ML solutions and optimize models for real-world applications.<br>
        Explore my portfolio to see some of my projects!</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.markdown("---")

# Projects Section
project_section = create_project_section(projects)
st.markdown(project_section, unsafe_allow_html=True)
