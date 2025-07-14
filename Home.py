import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests
import random
from random import randrange

st.header("DnD Database and Charactermaker")
st.subheader("This is the homepage. To navigate use the sidebar.")

def random(list):
    return(randrange(len(list)))

page_list = ['Home.py', 'Character_Creation.py', 'Story_Planner_Page.py', 'Spell_Overview_Page.py', 'Monster_Overview_Page.py']

page = (page_list[random(page_list)])

st.write(f"You might want to check out this page:")
st.page_link(page)
st.write(f"You can also access it from the navigation menu on the side of the screen.")
#st.page_link("file.py")