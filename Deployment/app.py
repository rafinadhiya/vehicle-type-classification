import streamlit as st
import eda
import prediction

# Sidebar untuk navigasi
navigation = st.sidebar.selectbox('Pilih Halaman:', ('predictor', 'eda'))

# Pilihan navigasi
if navigation == 'predictor':
    prediction.run()
else:
    eda.run()
