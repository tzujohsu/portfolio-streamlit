# streamlit sqlite3 dependency handling
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# streamlit torch dependency handling
import torch
torch.classes.__path__ = []


import streamlit as st
from st_pages import get_nav_from_toml
st.set_page_config(page_title="Jocelyn Hsu - Portfolio", layout="wide")

nav = get_nav_from_toml(
    ".streamlit/pages.toml"
)

pg = st.navigation(nav)

pg.run()
