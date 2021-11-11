from numpy import int0
import SessionState
import pandas as pd
import streamlit as st

# Number of entries per screen

st.markdown("# Demonstrating use of Next button with Session State")
st.sidebar.header('Filters')
entries = st.sidebar.number_input("Entries", value=15)
# default value = 15
N = entries

collection = st.sidebar.text_input("Collection")

# A variable to keep track of which product we are currently displaying
session_state = SessionState.get(page_number = 0)

data = pd.read_csv("nifty_mint.csv")
last_page = len(data) // N

# Add a next button and a previous button

prev, _ ,next = st.columns([1, 10, 1])

if next.button("Next"):

    if session_state.page_number + 1 > last_page:
        session_state.page_number = 0
    else:
        session_state.page_number += 1

if prev.button("Previous"):

    if session_state.page_number - 1 < 0:
        session_state.page_number = last_page
    else:
        session_state.page_number -= 1

# Get start and end indices of the next page of the dataframe
start_idx = session_state.page_number * N 
end_idx = (1 + session_state.page_number) * N

# Index into the sub dataframe
sub_df = data.iloc[start_idx:end_idx]
st.write(sub_df)