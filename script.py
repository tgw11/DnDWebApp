import streamlit as st

st.set_page_config(
    page_title="DnD//Streamlit Website",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

pg = st.navigation(['Home.py', 'Character_Creation.py', 'Story_Planner_Page.py', 'Spell_Overview_Page.py', 'Monster_Overview_Page.py'])
pg.run()