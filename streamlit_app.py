import pandas as pd
import streamlit as st

sohdf = pd.read_csv('sohdata.csv')
st.line_chart(sohdf, x="Date", y="SoH")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
