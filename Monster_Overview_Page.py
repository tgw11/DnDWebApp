import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests

def page_monsters():
    st.title("Monster Data")


baseurl = "https://www.dnd5eapi.co"
df = pd.read_csv("monsters.csv")

if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])

df["full_url"] = baseurl + df["url"]

base_columns = ["name", "size", "type", "alignment", "hit_points", "full_url"]
new_df = df[base_columns]

st.header("DnD Monster-Dataframe")
st.dataframe(new_df)

monster_view = st.number_input(
        "Input the Number of the Monster you'd like to know more about",
        min_value=0,
        max_value=len(df) - 1,
        step=1,
        format="%d"
    )

def display_image(index):
    img = requests.get(baseurl + df["image"][index])
    image = Image.open(BytesIO(img.content))
    return image

if st.button("Show Monster Info"):
    selected_row = df.iloc[int(monster_view)]
    st.header(f"{selected_row['name']}")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Image of the selected Monster")
        st.image(display_image(monster_view))
    with col2:
        st.subheader("Info about the selected Monster")
        st.dataframe(selected_row.to_frame(name="Value"), height=800)