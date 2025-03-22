import os
import streamlit as st

file_path = "movie.xlsx"

if os.path.exists(file_path):
    st.success("✅ File exists!")
else:
    st.error(f"❌ File NOT found in Streamlit Cloud! Current directory: {os.getcwd()}")
    st.write("Files in this directory:", os.listdir())
