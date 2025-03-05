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
            <h3><strong>also known as Jocelyn.</h3>
            <p>I'm a Data Scientist passionate about leveraging analytics and machine learning to solve cool challenges.</p>
            <p>My interests span data analysis, predictive modeling, and scalable systems.</p>
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

# st.markdown("---")

# # Skills Section
