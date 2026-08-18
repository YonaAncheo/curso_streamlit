import streamlit as st
import pandas as pd

df = pd.read_csv('es.2.csv')

def main():

  """
  st.header("esto es una Header")
  st.subheader("esto es un sub header")
  st.text("hola, estos es un texto")
  nombre = "yona"
  st.text(f"hola {nombre}, esto es otro texto")
  st.markdown("### Este es un texto con markdown")

  st.success("exito")
  st.warning("ADVERTENCIA")
  st.info("Información importante")
  st.error("esto es un ERRROR")
  st.exception("Estos es una EXCEPCIÓN")
  

  
  st.title("Curso Streamlit")
  st.write("texto normal")
  st.write("## Esto es un texto con Markdown")
  st.write(1+2)
  
  st.title("Curso Streamlit")
  st.header("DataFrame:")
  ##st.dataframe(df)
  ##st.dataframe(df.style.highlight_max(axis=0))
  st.dataframe(df.head(10))
  st.json({"clave":"valor"})

  #codigo =
  #  def saludar():
  #    print('hola')
  st.code(codigo, language="python")

  # SELECT BOX
    opcion = st.selectbox(
      'Elige tu equipo favorito',
      ["colo colo", "u de chile", "u catolica"]
    )
    st.write("El equipo seleccionado es:", opcion)
  
    # MULTISELECT
    opcion = st.multiselect(
        'Elige tu equipo favorito',
        ["colo colo", "u de chile", "u catolica"]
      )
    st.write("El equipo seleccionado es:", opcion)
  
    # SLIDER
    edad = st.slider(
      "Selecciona tu edad",
      min_value = 0,
      max_value = 100,
      value = 25,
      step = 1
    )
    st.write(f"tu edad es {edad}")
  """

  st.title("Curso de Streamlit")
  nombre = st.text_input("ingresa tu nombre")
  st.write(nombre)

  mensaje = st.text_area("ingresa tu mensaje: ",height=100)
  st.write(mensaje)

  numero = st.number_input("selecciona un numero", 1,25, step=1)
  st.write(numero)

  cita = st.date_input("selecciona una fecha")
  st.write(cita)

  hora = st.time_input("selecciona una hora")
  st.write(hora)

  color = st.color_picker("selecciona un color")
  st.write(color)

if __name__ == '__main__':
  main()

