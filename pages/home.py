import streamlit as st
from css import css, experience_css, education_css, experience_card_template
from portfolio_data import *
from utils.components import *
from streamlit_lottie import st_lottie

from datetime import datetime
import pandas as pd
import base64


# Apply CSS
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Intro
_, col1, col2, _ = st.columns([2, 4, 4, 1])
with col1:
    st.markdown(
        """
        <style>
        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }

        @keyframes blink {
            from, to { border-color: transparent }
            50% { border-color: orange; }
        }

        .typing-effect {
            overflow: hidden;
            white-space: nowrap;
            display: inline-block;
            position: relative;
            animation: typing 3.5s steps(40, end);
            font-size: 2.5rem !important;
        }

        .typing-effect::after {
            content: "";
            position: absolute;
            right: 0;
            top: 0;
            bottom: 0;
            width: 3px;
            background: orange;
            animation: blink .75s step-end infinite, 
                    hide-cursor 0s 2.4s forwards;
        }

        @keyframes hide-cursor {
            to { opacity: 0; }
        }
        </style>

        <div style="text-align: left;">
            <h1 class="typing-effect"><strong>Hi, I'm Tzu-Jo Hsu</strong></h1>
            <h3><strong>I also go by Jocelyn.</h3>
            <p>I'm a Data Scientist passionate about leveraging analytics and machine learning to solve cool challenges.</p>
            <p>My interests span data analysis, predictive modeling, and information retrieval.</p>
            <p>Explore my portfolio to see projects where I drive impact through AI and data!</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

# Profile Picture

with col2:
    # lottie_url = 'https://lottie.host/61a7a446-fd25-4d9d-942e-c6488aaf4e0c/ql1mK101vy.json'
    # st_lottie(lottie_url, key="user", height=300, speed=1)
    file_ = open('img/jo.JPG', "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(f'''
        <br> 
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{data_url}" 
                 alt="Jocelyn" 
                 style="max-width: 260px; width: 100%; height: auto;">
        </div>
    ''', unsafe_allow_html=True)
    
st.markdown("---")

# Projects Section
project_section = create_project_section(projects)
st.markdown(project_section, unsafe_allow_html=True)

st.markdown("---")

# Experience Section

# Function to generate the experience card
def generate_experience_card(exp):
    # Determine whether to use image or placeholder for logo
    if exp.get('logo') and exp['logo'].strip():
        
        file_ = open(exp.get('logo'), "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        # <img src="data:image/png;base64,{data_url}">
        logo_html = f'<div class="company-logo"><img src="data:image/png;base64,{data_url}" alt="{exp["company"]} logo" /></div>'
    else:
        logo_html = f'<div class="logo-placeholder" style="background-color: {exp["color"]}; color: white;">{exp["logo_initial"]}</div>'
    
    highlights_html = "".join([f'<span class="highlight-tag">{tag}</span>' for tag in exp['highlights']])
    department = f" - {exp['department']}" if exp.get('department') else ""
    
    # Replace placeholders with actual values
    rendered_card = experience_card_template.format(
        role=exp['role'],
        company=exp['company'],
        department=department,
        duration=exp['duration'],
        tenure=exp['tenure'],
        location=exp['location'],
        type=exp['type'],
        description=exp['description'],
        logo_html=logo_html,
        highlights_html=highlights_html
    )
    
    return rendered_card

def experience_section():
    # Add custom CSS for styling
    st.markdown(experience_css, unsafe_allow_html=True)
    # Main experience section
    st.markdown('<h3 class="section-title">🚀 PROFESSIONAL JOURNEY</h3>', unsafe_allow_html=True)
    st.markdown('<div class="experience-container">', unsafe_allow_html=True)
    for exp in experiences:
        st.markdown(generate_experience_card(exp), unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True) 

_, col1, _ = st.columns([2, 6, 2])
with col1:
    experience_section()
    st.markdown("---")

# Education Section

def generate_education_card(exp):
    if exp.get('logo') and exp['logo'].strip():
        file_ = open(exp.get('logo'), "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        logo_html = f'<div class="education-logo"><img src="data:image/png;base64,{data_url}" alt="{exp["university"]} logo" /></div>'
    else:
        logo_html = f'''<div class="education-logo"><div class="logo-placeholder" style="background-color: {exp['color']}; color: white;">{exp['logo_initial']}</div></div>'''

    
    return f'''
    <div class="education-card">
        <div class="education-details">
            <div class="university-name">{exp['university']}</div>
            <div class="degree">{exp['degree']}</div>
            <div class="duration">
                <span>🗓️</span>
                <span>{exp['duration']}</span>
            </div>
        </div>
        {logo_html}
    </div>
    '''

def education_section():
    st.markdown(education_css, unsafe_allow_html=True)
    st.markdown('<h3 class="education-section-title">🎓 EDUCATION</h3>', unsafe_allow_html=True)
    st.markdown('<div class="education-container">', unsafe_allow_html=True)

    for edu in education:
        st.markdown(generate_education_card(edu), unsafe_allow_html=True)
    
    

    st.markdown('</div>', unsafe_allow_html=True)
_, col1, _ = st.columns([2, 6, 2])
with col1:
    education_section()
    st.markdown("---")

# Skills Section

_, col1, _ = st.columns([2, 6, 2])
with col1:
    st.markdown(f"<div class='title'><h3>🛠️ HIGHLIGHTED SKILLS</h3></div>",unsafe_allow_html=True)
    st.markdown("""
    <style>
    .highlight {
        background-color: rgba(16, 109, 156, 0.2);  
        padding: 0 0.4rem;
        border-radius: 0.25rem;
        font-weight: bold;
        line-height: 1.5;
    }
    """,
    unsafe_allow_html=True
    )

    # Skills Dictionary
    skills = {
        "📊 Data Science & Analytics": ["Predictive Modeling", "Statistical Analysis", 'LLM', 'NLP'],
        "⚙️ Programming & Engineering": ["Python", "R", "SQL", "APIs", "ETL"],
        "☁️ Cloud & DevOps": ["AWS", "Docker", "FastAPI", "MLFlow", "SQL Server", "MySQL", "Linux"],
        "📈 Data Visualization & BI": ["Tableau", "Looker Studio", "Matplotlib", "Seaborn"]
    }

    # Display Skills with Highlighting
    for category, tools in skills.items():
        st.markdown(f"**{category}**")
        highlighted_skills = "  ".join([f"<span class='highlight'>{skill}</span>" for skill in tools])
        st.markdown(f"{highlighted_skills}", unsafe_allow_html=True)

st.markdown("---")

def display_contact():
    
    # Display the contact badges at the end
    contact_info = """
    <style>
        .contact-badges {
            display: flex;
            gap: 18px;
            justify-content: center;
            margin-top: 20px;
        }
        .contact-badges a {
            text-decoration: none;
            color: inherit;
        }
        .contact-badges img {
            width: 40px;
            height: 40px;
            border-radius: 8px;
            transition: transform 0.2s ease-in-out;
        }
        .contact-badges img:hover {
            transform: scale(1.1);
        }
    </style>
    <h5 class="section-title">٩(>w<)و Contact Me</h5>
    <div class="contact-badges">
        <a href="mailto:jocelynhsu.tjh@gmail.com" target="_blank">
            <img src="https://img.icons8.com/color/48/apple-mail.png" alt="Email">
        </a>
        <a href="https://www.linkedin.com/in/jocelyn-hsu-78518828b/" target="_blank">
            <img src="https://img.icons8.com/fluency/48/000000/linkedin.png" alt="LinkedIn">
        </a>
        <a href="https://github.com/tzujohsu" target="_blank">
            <img src="https://img.icons8.com/fluency/48/000000/github.png" alt="GitHub">
        </a>
    </div>
    """
    st.markdown(contact_info, unsafe_allow_html=True)
display_contact()