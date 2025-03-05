__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import torch
torch.classes.__path__ = []

import streamlit as st
from st_pages import get_nav_from_toml
st.set_page_config(page_title="Jocelyn Hsu - Portfolio", layout="wide")


# sections = st.sidebar.toggle("Sections", value=True, key="use_sections")

nav = get_nav_from_toml(
    ".streamlit/pages.toml"
)

pg = st.navigation(nav)

pg.run()
