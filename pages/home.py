import streamlit as st
from css import css
from projects import *
from utils.components import *
from streamlit_lottie import st_lottie


# Apply CSS
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
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
with col2:
    lottie_url = 'https://lottie.host/61a7a446-fd25-4d9d-942e-c6488aaf4e0c/ql1mK101vy.json'
    st_lottie(lottie_url, key="user", height=300, speed=1)

st.markdown("---")

# Projects Section
project_section = create_project_section(projects)
st.markdown(project_section, unsafe_allow_html=True)

st.markdown("---")

# # Skills Section

# st.subheader("🛠️ Technical Skills")
_, col1, _ = st.columns([1, 7, 1])

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
        "☁️ Cloud & DevOps": ["AWS (SageMaker, EC2, S3)", "Docker", "FastAPI", "MLFlow", "SQL Server", "MySQL", "Linux"],
        "📈 Data Visualization & BI": ["Tableau", "Looker Studio", "Matplotlib", "Seaborn"]
    }

    # Display Skills with Highlighting
    for category, tools in skills.items():
        st.markdown(f"**{category}**")
        highlighted_skills = "  ".join([f"<span class='highlight'>{skill}</span>" for skill in tools])
        st.markdown(f"{highlighted_skills}", unsafe_allow_html=True)

# Optional: Add a subtle horizontal line for separation
st.markdown("---")
