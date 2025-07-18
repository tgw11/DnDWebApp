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
    number = st.selectbox("Number of choices:", (1, 2, 3, 4, 5))
    with st.form("Beginning of the Story", clear_on_submit=True):
        title = st.text_input("Input the title of this part of the story", value='empty')
        text = st.text_input("Input the first sentence of the game",value='empty')
        if number == 1:
            choice = st.text_input("Choice 1", value='empty')
            consq = st.text_input("Consequence 1", value='empty')
            choice2 = 'empty'
            consq2 = 'empty'
            choice3 = 'empty'
            consq3 = 'empty'
            choice4 = 'empty'
            consq4 = 'empty'
            choice5 = 'empty'
            consq5 = 'empty'
        elif number == 2:
            choice = st.text_input("Choice 1", value= 'empty')
            consq = st.text_input("Consequence 1", value= 'empty')
            choice2 = st.text_input("Choice 2", value= 'empty')
            consq2 = st.text_input("Consequence 2", value= 'empty')
            choice3 = 'empty'
            consq3 = 'empty'
            choice4 = 'empty'
            consq4 = 'empty'
            choice5 = 'empty'
            consq5 = 'empty'
        elif number == 3:
            choice = st.text_input("Choice 1", value='empty')
            consq = st.text_input("Consequence 1", value='empty')
            choice2 = st.text_input("Choice 2", value='empty')
            consq2 = st.text_input("Consequence 2", value='empty')
            choice3 = st.text_input("Choice 3", value='empty')
            consq3 = st.text_input("Consequence 3", value='empty')
            choice4 = 'empty'
            consq4 = 'empty'
            choice5 = 'empty'
            consq5 = 'empty'
        elif number == 4:
            choice = st.text_input("Choice 1", value='empty')
            consq = st.text_input("Consequence 1", value='empty')
            choice2 = st.text_input("Choice 2", value='empty')
            consq2 = st.text_input("Consequence 2", value='empty')
            choice3 = st.text_input("Choice 3", value='empty')
            consq3 = st.text_input("Consequence 3", value='empty')
            choice4 = st.text_input("Choice 4", value='empty')
            consq4 = st.text_input("Consequence 4", value='empty')
            choice5 = 'empty'
            consq5 = 'empty'
        elif number == 5:
            choice = st.text_input("Choice 1", value='empty')
            consq = st.text_input("Consequence 1", value='empty')
            choice2 = st.text_input("Choice 2", value='empty')
            consq2 = st.text_input("Consequence 2", value='empty')
            choice3 = st.text_input("Choice 3", value='empty')
            consq3 = st.text_input("Consequence 3", value='empty')
            choice4 = st.text_input("Choice 4", value='empty')
            consq4 = st.text_input("Consequence 4", value='empty')
            choice5 = st.text_input("Choice 5", value='empty')
            consq5 = st.text_input("Consequence 5", value='empty')
        save = st.form_submit_button("Save 'Beginning of the Story'")

        if save:
            datas1 = {
                "Title": title,
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

if st.session_state.mode == 'game':
    if 'view1' not in st.session_state:
        st.session_state.view1 = True
    if 'chosen_story' not in st.session_state:
        st.session_state.chosen_story = None

    success = True
    try:
        file_beg = pd.read_csv("beginning.csv")
    except:
        success = False
        st.error("There is no data to continue with. Please create a story first.")

    if success:
        if st.session_state.view1:
            col3, col4 = st.columns(2)
            with col3:
                st.write(file_beg['Title'].reset_index(drop=True))
            with col4: 
                options = file_beg['Title'].tolist()
                with st.form("Story viewer select"):
                    chosen_story = st.selectbox('Select the Story you want to view', options)
                    submit = st.form_submit_button("Confirm")

                if submit:
                    st.session_state.view1 = False
                    st.session_state.index  = chosen_story

        else:
            spec_df = file_beg[file_beg['Title'] == st.session_state.chosen_story]
            if not spec_df.empty:
                row = spec_df.iloc[0]
                display_df = row.to_frame(name="Value")

                display_df = display_df[display_df["Value"] != "empty"]
                st.dataframe(display_df)
            else:
                st.warning("No matching story found.")
            if st.button('Select different story'):
                st.session_state.view1 = True
                st.session_state.chosen_story = None

