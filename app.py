import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado de la aplicación
st.header('Análisis de Datos de Vehículos')

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear casillas de verificación para seleccionar los gráficos
show_histogram = st.checkbox('Construir histograma')
show_scatter = st.checkbox('Construir gráfico de dispersión')

if show_histogram:
    # Mostrar un mensaje al usuario
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma de la columna "odometer"
    fig = px.histogram(car_data, x="odometer",
                       title="Distribución del Odómetro")

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)

if show_scatter:
    # Mostrar un mensaje al usuario
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión de "odometer" vs "price"
    scatter_fig = px.scatter(
        car_data, x="odometer", y="price", title="Relación entre Odómetro y Precio")

    # Mostrar el gráfico interactivo
    st.plotly_chart(scatter_fig, use_container_width=True)
