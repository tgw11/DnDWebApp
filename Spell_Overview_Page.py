import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests


def page_spells():
    st.title("Spell Data")


baseurl = "https://www.dnd5eapi.co"
df = pd.read_csv("spells.csv")

if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])

df["full_url"] = baseurl + df["url"]

base_columns = ["name", "level", "range", "ritual", "full_url"]
new_df = df[base_columns]

st.header("DnD Spell-Dataframe")
st.dataframe(new_df)

spell_view = st.number_input(
        "Input the Number of the Spell you'd like to know more about",
        min_value=0,
        max_value=len(df) - 1,
        step=1,
        format="%d"
    )

if st.button("Show Spell Info"):
    selected_row = df.iloc[int(spell_view)]
    st.header(f"{selected_row['name']}")
    st.subheader("Info about the selected Spell")
    st.dataframe(selected_row.to_frame(name="Value"))