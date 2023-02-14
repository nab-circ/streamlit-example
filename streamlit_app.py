import pandas as pd
import streamlit as st
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

#sohdf = pd.read_csv('sohdata.csv', parse_dates=['Date'])
#st.line_chart(sohdf, x="Date", y="SoH")

sohdf_b = pd.read_csv('sohdata.csv', parse_dates=['Date'])
source = ColumnDataSource(sohdf_b)

p = figure(title="Battery SoH", x_axis_type="datetime", x_axis_label='Time', y_axis_label='SoH(%)', y_range=(70, 100), tools=['pan', 'wheel_zoom', "reset"], plot_width=400, plot_height=250)
p.x_range.bounds=(min(sohdf_b['Date']),max(sohdf_b['Date']))
p.y_range.bounds=(0,120)
p.xgrid.visible = False
p.line(x='Date', y='SoH', line_width=2, source=source)

p.toolbar.logo = None
# p.toolbar_location = None
st.bokeh_chart(p, use_container_width=True)


sohdf_dis = pd.read_csv('soh_discharge_capacity.csv')
source2 = ColumnDataSource(sohdf_dis)

p2 = figure(title="Battery Capacity Fade", x_axis_label='Cycle', y_axis_label='Battery Capacity(Ah)', y_range=(20, 30), tools=['pan', 'wheel_zoom', "reset"], plot_width=400, plot_height=250)
p2.x_range.bounds=(1,150)
p2.y_range.bounds=(10,40)
p2.xgrid.visible = False
p2.line(x='Cycle', y='Discharge Capacity (Ah)', line_width=2, source=source2)

p2.toolbar.logo = None
# p.toolbar_location = None
st.bokeh_chart(p2, use_container_width=True)


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        a {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
