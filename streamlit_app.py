import pandas as pd
import streamlit as st
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

sohdf = pd.read_csv('sohdata.csv', parse_dates=['Date'])
st.line_chart(sohdf, x="Date", y="SoH")

sohdf_b = pd.read_csv('sohdata.csv', parse_dates=['Date'])
source = ColumnDataSource(sohdf_b)

p = figure(x_axis_type="datetime", x_axis_label='Time', y_axis_label='SoH(%)', y_range=(70, 100), tools=['pan', 'wheel_zoom', "box_zoom", "reset"], plot_width=400, plot_height=200)
p.line(x='Date', y='SoH', line_width=2, source=source)

p.toolbar.logo = None
# p.toolbar_location = None
st.bokeh_chart(p, use_container_width=True)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        a {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
