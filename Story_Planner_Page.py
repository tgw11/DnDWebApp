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
    with st.form("Beginning of the Story", clear_on_submit=True):
        text = st.text_input("Input the first sentence of the game", value="You find yourself on a lively market")
        choice1 = st.text_input("Choice 1", value="Check out the vendors at the market")
        consq1 = st.text_input("Consequence 1", value="One vendor makes buy smth (-50g, +'rusty sword')")
        choice2 = st.text_input("Choice 2", value="Plan the adventure in the Tavern at the corner")
        consq2 = st.text_input("Consequence 2", value="*Option buttons: location 1, location2, ...*")
        save = st.form_submit_button("Save 'Beginning of the Story'")

        if save:
            datas1 = {
                "Sentence": text,
                "Choice1": choice1,
                "Consequence1": consq1,
                "Choice2": choice2,
                "Consequence2": consq2
            }

            save_element(datas1, file_beg)
            st.success("✅ Saved successfully!")
