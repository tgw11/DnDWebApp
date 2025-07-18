import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests
import os

df_sp = pd.read_csv("spells.csv")
spell_list = df_sp['name'].tolist()
spell_list.append("None")

CSV_FILE = "character_sheets.csv"

if os.path.exists(CSV_FILE):
    try:
        df_char = pd.read_csv(CSV_FILE)
    except pd.errors.EmptyDataError:
        df_char = pd.DataFrame()
else:
    df_char = pd.DataFrame()

def clear_characters(file_path):
    columns = [
        "Name", "Age", "Party", "Class", "Alignment", "Background", "Ideals",
        "Bonds", "Gender", "Eyecolor", "Haircolor1", "Haircolor2", "Skincolor",
        "Height (m)", "Weight (kg)", "Traits", "Social Skill", "Spells"
    ]
    pd.DataFrame(columns=columns).to_csv(file_path, index=False)

def save_character(data, file_path):
    df_char = pd.DataFrame([data])
    
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        df_char.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df_char.to_csv(file_path, index=False)

with st.form("character_form"):
    st.write("Character Sheet")
    name = st.text_input('Character Name:')
    age = st.number_input('Character Age:')
    party = st.text_input('Characters Adventuring Party:')
    option = st.selectbox(
        "Class",
        ("Select", "barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rouge", "sorcerer", "warlock", "wizard"),
    )
    option2 = st.selectbox(
        "Alignment",
        ("Select", "lawful good", "neutral good", "chaotic good", "lawful neutral", "true neutral", "chaotic neutral", "lawful evil", "neutral evil", "chaotic evil"),
    )
    txt1 = st.text_area('Character Background:')
    txt2 = st.text_area('Ideals:')
    txt3 = st.text_area('Bonds:')
    option3 = st.selectbox(
        "Gender",
        ("Select", "Female", "Male", "Non-Binary", "Other"),
    )
    eyecolor = st.color_picker("Character Eyecolor")
    haircolor1 = st.color_picker("Character Haircolor (primary)")
    haircolor2 = st.color_picker("Character Haircolor (secondary)")

    skincolor = st.color_picker("Character Skincolor")

    height = st.number_input("Character Height in m")
    st.write(height, "m")

    weight = st.number_input("Character Weight in kg")
    st.write(weight, "kg")

    traits = st.multiselect(
        "Characters Personal Traits:",
        ["-", "Nice", "Kind", "Cheerful", "Energetic", "Friendly", "Cutesy", "Easily annoyed", "Chaotic", "Open", "Easily distracted", "Smart", "Intelligent", "Social", "Angry", "Crazy", "Insane", "Silly", "Bored", "Merciless", "Raging", "Adorable", "Mean", "Beloved", "Antisocial", "Active", "Adventorous", "Admirable", "Athletic", "Calm", "Attractive", "Caring", "Confident"],
        default=["-"],
    )

    option4 = st.selectbox(
        "Characters Social Skills",
        ("Select", 'Extrovert', 'Ambivert', "Introvert"),
    )
    spells = st.multiselect(
        "Characters Spells:",
        spell_list,
    )

    submit = st.form_submit_button('Save Character Sheet')
if submit: 
    character_data = {
        "Name": name,
        "Age": age,
        "Party": party,
        "Class": option,
        "Alignment": option2,
        "Background": txt1,
        "Ideals": txt2,
        "Bonds": txt3,
        "Gender": option3,
        "Eyecolor": eyecolor,
        "Haircolor1": haircolor1,
        "Haircolor2": haircolor2,
        "Skincolor": skincolor,
        "Height (m)": height,
        "Weight (kg)": weight,
        "Traits": "; ".join(traits),
        "Social Skill": option4,
        "Spells": "; ".join(spells),
    }

    save_character(character_data, CSV_FILE) 
    st.success(f"Character '{name}' saved successfully!")

df_char = pd.read_csv("character_sheets.csv")

if df_char.empty:
    st.warning("No made characters available.")
else:
    if st.button('Access previously made Characters'):
        st.dataframe(df_char)

    if st.button('Clear previously made Characters'):
        clear_characters(CSV_FILE)
        st.success("Characters cleared (headers preserved).")
        st.stop()

    character_edit = st.number_input(
        "Input the Number of the Character you'd like to edit",
        min_value=0,
        max_value=len(df_char) - 1,
        step=1,
        format="%d"
    )

    selected_character = df_char.iloc[character_edit]

    if st.button(f"Edit {selected_character['Name']}"):
        with st.form("edit_character"):
            st.write(f"Editing Character {selected_character['Name']}")

            name = st.text_input('Character Name:', value=selected_character["Name"])
            age = st.number_input('Character Age:', value=selected_character["Age"])
            party = st.text_input('Characters Adventuring Party:', value=selected_character["Party"])
            char_class = st.text_input('Class:', value=selected_character["Class"])
            alignment = st.text_input('Alignment:', value=selected_character["Alignment"])
            background = st.text_area('Background:', value=selected_character["Background"])
            ideals = st.text_area('Ideals:', value=selected_character["Ideals"])
            bonds = st.text_area('Bonds:', value=selected_character["Bonds"])
            gender = st.text_input('Gender:', value=selected_character["Gender"])
            eyecolor = st.color_picker("Eyecolor", value=selected_character["Eyecolor"])
            hair1 = st.color_picker("Haircolor1", value=selected_character["Haircolor1"])
            hair2 = st.color_picker("Haircolor2", value=selected_character["Haircolor2"])
            skin = st.color_picker("Skincolor", value=selected_character["Skincolor"])
            height = st.number_input("Height (m)", value=float(selected_character["Height (m)"]))
            weight = st.number_input("Weight (kg)", value=float(selected_character["Weight (kg)"]))
            traits = st.text_input("Traits (semicolon separated):", value=selected_character["Traits"])
            social = st.text_input("Social Skill:", value=selected_character["Social Skill"])
            spells = st.text_input("Spells (semicolon separated):", value=selected_character["Spells"])

            save_edit = st.form_submit_button("Save Edits")

            if save_edit:
                df_char.loc[character_edit] = {
                    "Name": name,
                    "Age": age,
                    "Party": party,
                    "Class": char_class,
                    "Alignment": alignment,
                    "Background": background,
                    "Ideals": ideals,
                    "Bonds": bonds,
                    "Gender": gender,
                    "Eyecolor": eyecolor,
                    "Haircolor1": hair1,
                    "Haircolor2": hair2,
                    "Skincolor": skin,
                    "Height (m)": height,
                    "Weight (kg)": weight,
                    "Traits": traits,
                    "Social Skill": social,
                    "Spells": spells,
                }
                df_char.to_csv(CSV_FILE, index=False)
                st.success(f"Character #{character_edit} updated successfully!")