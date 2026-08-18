# PARA CORRER UNA APP STREAMLIT, SE DEBE DESPLEGAR CON streamlit run app.py
# Documentación Streamlit
# https://docs.streamlit.io/get-started/tutorials/create-an-app
import streamlit as st
import pandas as pd

st.set_page_config(page_title='YonApp', page_icon="smile", layout="wide", initial_sidebar_state="collapsed")

def main():
  st.title("Bienvenidos a mi Código Yona")
  st.sidebar.header("Navegación")
  df = pd.read_csv("es.2.csv")
  st.dataframe(df)

if __name__  == '__main__':
  main()