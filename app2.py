# PARA CORRER UNA APP STREAMLIT, SE DEBE DESPLEGAR CON streamlit run app.py
# Documentación Streamlit
# https://docs.streamlit.io/get-started/tutorials/create-an-app
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='YonApp', page_icon="smile", layout="wide", initial_sidebar_state="collapsed")

def main():
  st.title("Bienvenidos a mi Código Yona")
  st.sidebar.header("Navegación")
  df = pd.read_csv("es.2.csv")
  st.dataframe(df)
  df_count = df.groupby('Team 1').count().reset_index()
  #df_count = df['Team 1'].value_counts()
  fig = px.pie(df_count, values="Team 2", names="Team 1", title="Equipos")
  st.plotly_chart(fig)

if __name__  == '__main__':
  main()