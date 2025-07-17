import streamlit as st
import pandas as pd
import os

st.title("Story Planner")
st.header("This Page helps you plan your Story and the choices players can make.")

file_beg = "beginning.CSV"

def save_element(data, file_path):
    df = pd.DataFrame([data])
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, index=False)


if "mode" not in st.session_state:
    st.session_state.mode = None

col1, col2 = st.columns(2)
with col1:
    if st.button("Editor Mode"):
        st.session_state.mode = "edit"
with col2:
    if st.button("Game Mode"):
        st.session_state.mode = "game"

st.caption(f"📁 Current working directory: `{os.getcwd()}`")

if st.session_state.mode == "edit":
    number = st.selectbox("Input here:", (1, 2, 3, 4, 5))
    with st.form("Beginning of the Story", clear_on_submit=True):
        text = st.text_input("Input the first sentence of the game", value="You find yourself on a lively market")
        if number == 1:
            choice = st.text_input("Choice 1")
            consq = st.text_input("Consequence 1")
        elif number == 2:
            choice = st.text_input("Choice 1")
            consq = st.text_input("Consequence 1")
            choice2 = st.text_input("Choice 2")
            consq2 = st.text_input("Consequence 2")
        elif number == 3:
            choice = st.text_input("Choice 1")
            consq = st.text_input("Consequence 1")
            choice2 = st.text_input("Choice 2")
            consq2 = st.text_input("Consequence 2")
            choice3 = st.text_input("Choice 3")
            consq3 = st.text_input("Consequence 3")
        elif number == 4:
            choice = st.text_input("Choice 1")
            consq = st.text_input("Consequence 1")
            choice2 = st.text_input("Choice 2")
            consq2 = st.text_input("Consequence 2")
            choice3 = st.text_input("Choice 3")
            consq3 = st.text_input("Consequence 3")
            choice4 = st.text_input("Choice 4")
            consq4 = st.text_input("Consequence 4")
        elif number == 5:
            choice = st.text_input("Choice 1")
            consq = st.text_input("Consequence 1")
            choice2 = st.text_input("Choice 2")
            consq2 = st.text_input("Consequence 2")
            choice3 = st.text_input("Choice 3")
            consq3 = st.text_input("Consequence 3")
            choice4 = st.text_input("Choice 4")
            consq4 = st.text_input("Consequence 4")
            choice5 = st.text_input("Choice 5")
            consq5 = st.text_input("Consequence 5")
        save = st.form_submit_button("Save 'Beginning of the Story'")

        if save:
            datas1 = {
                "Sentence": text,
                "Choice1": choice,
                "Consequence1": consq,
                "Choice2": choice2,
                "Consequence2": consq2,
                "Choice3": choice3,
                "Consequence3": consq3,
                "Choice4": choice4,
                "Consequence4": consq4,
                "Choice5": choice5,
                "Consequence5": consq5,

            }

            save_element(datas1, file_beg)
            st.success("✅ Saved successfully!")
