import pandas as pd
import plotly.express as px
import streamlit as st

coffee_data = pd.read_csv('ProdutosAutorizadosABIC.csv', sep=';')
coffee_data.columns = coffee_data.columns.str.lower().str.replace(' ', '_').str.replace('ç', 'c').str.replace('ã', 'a').str.replace('í', 'i')

st.header('MEU PAU AZEDO')

prod_total = st.button('Produção por Estado')
prod_especial = st.button('Produção Por Estado - Categoria Especial')
prod_gourmet = st.button('Produção Por Estado - Categoria Gourmet')
prod_superior = st.button('Produção Por Estado - Categoria Superior')

if prod_total:
    st.write('Criando gráfico de Produção total por Estado')
    
    # Filtrando valores
    todos_por_estado = coffee_data['estado'].value_counts()
    
    # Criando gráficos
    fig = px.bar(
        todos_por_estado,
        title='Número de rótulos de café por Estado Brasileiro',
        labels={'estado': 'Estados Brasileiros', 'value': 'Quantitade de Rótulos'}
    )
    fig.update_traces(marker_color='red')
    st.plotly_chart(fig, width='stretch')

if prod_especial:
    st.write('Criando gráfico de Produção Especial por Estado')
    
    # Filtrando valores
    especial_por_estado = coffee_data['estado'][coffee_data['tipo_simbolo'] == 'Especial'].value_counts()
    
    # Criando gráficos
    fig = px.bar(
        especial_por_estado,
        title='Número de cafés "Especial" por Estado Brasileiro',
        labels={'Estado': 'Estados Brasileiros', 'value': 'Quantitade de Rótulos'}
    )
    fig.update_traces(marker_color='orange')
    st.plotly_chart(fig, width='stretch')

if prod_gourmet:
    st.write('Criando gráfico de Produção Gourmet por Estado')
    
    # Filtrando valores
    gourmet_por_estado = coffee_data['estado'][coffee_data['tipo_simbolo'] == 'Gourmet'].value_counts()
    
    # Criando gráficos
    fig = px.bar(
        gourmet_por_estado,
        title='Número de cafés "Gourmet" por Estado Brasileiro',
        labels={'estado': 'Estados Brasileiros', 'value': 'Quantitade de Rótulos'}
    )
    fig.update_traces(marker_color='blue')
    st.plotly_chart(fig, width='stretch')

if prod_superior:
    st.write('Criando gráfico de Produção Superior por Estado')
    
    # Filtrando valores
    superior_por_estado = coffee_data['estado'][coffee_data['tipo_simbolo'] == 'Superior'].value_counts()
    
    # Criando gráficos
    fig = px.bar(
        superior_por_estado,
        title='Número de cafés "Superior" por Estado Brasileiro',
        labels={'estado': 'Estados Brasileiros', 'value': 'Quantitade de Rótulos'}
    )
    fig.update_traces(marker_color='grey')
    st.plotly_chart(fig, width='stretch')