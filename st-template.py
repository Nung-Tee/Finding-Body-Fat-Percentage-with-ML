import streamlit as st
import pandas as pd


#---------0. Try the first web-app running in Streamlit----------#
st.text("Hello Streamlit and world")

#---------1. Text elements in Streamlit----------#
# Give your app a title


# Header


# Markdown


# Preformatted text


# Divider


#---------2. Data display elements (using sample.csv)----------#
df = pd.read_csv("heart.csv")


#---------3. Charting elements (using sample.csv)----------#
# Streamlit line plot


# Streamlit bar chart (by default, it is stacked bar chart)


#---------4. Input widgets----------#
# Buttons



# Checkbox


# Radio buttons


# Selectbox


# Slider



#---------5. Sidebar in Streamlit----------#
# Sidebar
with st.sidebar:
    st.write("Text in the sidebar")