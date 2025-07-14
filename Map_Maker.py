import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests
import os

# --- Config ---
GRID_ROWS = 5
GRID_COLS = 5
CSV_FILE = "map.csv"
TILES = {
    "Grass 🟩": "🟩",
    "Water 🟦": "🟦",
    "Wall ⬛": "⬛",
    "Dirt 🟫": "🟫",
    "Empty ⬜": "⬜",
}

# --- Grid Management ---
def init_grid():
    if "grid" not in st.session_state:
        st.session_state.grid = [["⬜" for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

def reset_grid():
    st.session_state.grid = [["⬜" for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

def save_grid():
    df = pd.DataFrame(st.session_state.grid)
    df.to_csv(CSV_FILE, index=False)
    st.success("Grid saved to map.csv")

def load_grid():
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        st.session_state.grid = df.values.tolist()
        st.success("Grid loaded from map.csv")
    else:
        st.warning("No saved map found.")

# --- UI Components ---
def tile_selector():
    return TILES[st.radio("Select tile", list(TILES.keys()), horizontal=True)]

def render_grid(selected_tile):
    clicked = None  # Store which button was clicked

    for row_index, row in enumerate(st.session_state.grid):
        cols = st.columns(GRID_COLS)
        for col_index, col in enumerate(cols):
            tile = row[col_index]
            if col.button(tile, key=f"{row_index}-{col_index}", type="tertiary"):
                clicked = (row_index, col_index)

    # Do the update after rendering to avoid double-click issues
    if clicked:
        r, c = clicked
        st.session_state.grid[r][c] = selected_tile
        st.rerun()  # Rerun immediately to reflect change


# --- Main App ---
def main():
    st.title("🗺️ Emoji Tile Grid Editor")

    init_grid()
    selected_tile = tile_selector()

    st.write("Click a tile to place:", selected_tile)
    render_grid(selected_tile)

    st.markdown("### Actions")
    cols = st.columns(3)
    if cols[0].button("🔁 Reset"):
        reset_grid()
    if cols[1].button("💾 Save"):
        save_grid()
    if cols[2].button("📂 Load"):
        load_grid()

if __name__ == "__main__":
    main()