import streamlit as st
import pandas as pd
import preprocessor, helper

df = preprocessor.preprocess()
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete-wise Analysis')
)

st.dataframe(df)

if user_menu == 'Medal Tally':
    medal_telly = helper.medal_telly(df)
    st.dataframe(medal_telly)