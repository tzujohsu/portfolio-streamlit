import streamlit as st
from st_pages import add_page_title, get_nav_from_toml
import sys
__import__('pysqlite3')
import pysqlite3
sys.modules['sqlite3'] = sys.modules["pysqlite3"]

st.set_page_config(page_title="Jocelyn Hsu - Portfolio", layout="wide")


# sections = st.sidebar.toggle("Sections", value=True, key="use_sections")

nav = get_nav_from_toml(
    ".streamlit/pages.toml"
)

pg = st.navigation(nav)

pg.run()
