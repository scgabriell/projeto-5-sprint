import streamlit as st
import pandas as pd
import plotly.express as px
import scipy as sy

car_data = pd.read_csv("data/vehicles.csv") 

st.header("Título do Cabeçalho")

hist_button = st.button('Criar histograma') # criar um botão
        
if hist_button: # se o botão for clicado
            # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
            # criar um histograma
    fig = px.histogram(car_data, x="odometer")
        
            # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
    
    
sec_button = st.button('Criar grafico dispersão')
if sec_button:
    st.write('Criando um gráfico de dispersão')
    sec=px.scatter(car_data, x="odometer", y="price", title="Gráfico de Dispersão")
    st.plotly_chart(sec) 
    
    
first_select = st.checkbox("Mostrar histograma ")
if first_select:
        fig2 = px.histogram(car_data, x="odometer", title="Com o checkbox ativo ")
        st.plotly_chart(fig2, use_container_width=True)

else:
        sec=px.scatter(car_data, x="odometer", y="price", title="Sem o checkbox ativo ")
        st.plotly_chart(sec) 
                