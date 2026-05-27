import pandas as pd
import streamlit as st
import plotly_express as px

df = pd.read_csv('vehicles.csv')


# Configurações da UI
st.header('Dashboard - Sprint 5 - Gabriel Maldaner')
st.set_page_config(
    page_title='Dashboard - Gabriel Maldaner',
    layout='wide',
)

# Criando 2 widgets na UI
col1, col2 = st.columns(
    [1, 1],
    vertical_alignment='top',
    border=True,
    width='stretch'
    )

# Widget 1 = Menu com botões
with col1:
    button_hist = st.button('Criar Histograma - Odômetro')
    button_disp = st.button('Criar Dispersão - Preço vs Odômetro / Preço vs Ano Modelo')
    button_bar = st.button('Criar Barras - Número Tipos de Transmissão / Preço vs Transmissão')
        
    if button_hist:
        # Criando Histograma
        st.write('Criando Histograma')

        fig = px.histogram(
        df, 
        x='odometer',
        title='Histograma de Odômetros',
        color_discrete_sequence=['red'],
        labels={ 
            'odometer': 'Odômetro'
            }
        )
        st.plotly_chart(fig, width='stretch')


    if button_disp:
        
        # Gráfico Dispersão 1 - Preço vs Odômetro
        st.write('Criando Dispersão')

        fig1 = px.scatter(
        df, 
        x='odometer',
        y='price', 
        title='Dispersão entre Odômetro e Preço',
        color_discrete_sequence=['orange'],
        labels={
            'price': 'Preço (USD)', 
            'odometer': 'Odômetro'
            }
        )
        st.plotly_chart(fig1, width='stretch')

        # Gráfico Dispersão 2 - Preço vs Ano Modelo
        fig2 = px.scatter(
        df,
        x='model_year',
        y='price',
        title='Dispersão de Preços vs Ano Modelo',
        color_discrete_sequence=['blue'],
        labels={
            'model_year': 'Ano Modelo',
            'price': 'Preço (USD)',
            }
        )
        st.plotly_chart(fig2, width='stretch')

    if button_bar:
        # Gráfico Barras 1 - Número por tipo transmissão
        st.write('Criando Barras')

        df_contagem = df['transmission'].value_counts().reset_index()
        df_contagem.columns = ['transmission', 'contagem']

        fig1 = px.bar(
            df_contagem, 
            x='transmission',
            y='contagem',
            color='transmission',
            color_discrete_sequence=['blue', 'green', 'red'],
            text='contagem',
            title='Comparativo entre total de carros por cada tipo de transmissão',
            labels={
                'contagem': 'Número de Carros', 
                'transmission': 'Tipo de transmissão',
                }
        )
        fig1.update_traces(textposition='outside')
        st.plotly_chart(fig1, width='stretch')


        media_preco = df.groupby(by='transmission', as_index=False)['price'].mean()
        media_preco['price'] = media_preco['price'].round(2)

        fig2 = px.bar(
            media_preco, 
            x='transmission',
            y='price',
            text='price',
            barmode='group',
            color='transmission',
            color_discrete_sequence=['blue', 'green', 'red'],
            title='Média de preços por tipo de transmissão',
            labels={
                'price': 'Preço (USD)', 
                'transmission': 'Tipo de transmissão'
                }
        )
        fig2.update_traces(textposition='outside')
        st.plotly_chart(fig2, width='stretch')

# Widget 2 - Menu com multiselect
with col2:
    """
    Apesar de não precisar de todas as colunas, acho interessante deixar a opção assim
    para possível aproveitamento em outros parâmetros
    """

    selected_cols = st.multiselect(
    'HISTOGRAMAS DISPONÍVEIS - SELECIONAR ABAIXO',
    df.columns,
    )

    for col in selected_cols:
        # Selecionado somente categorias numéricas
        if col in ['price', 'odometer', 'model_year']:
            fig = px.histogram(
                df,
                x=col,
                title=f'Histograma de {col}',
                color_discrete_sequence=['red']
            )
            st.plotly_chart(fig, width='stretch')

        # Gerando warning para categorias que não geram histograma
        else:
            st.warning(f'Categoria "{col}" não disponível para Histogramas')

