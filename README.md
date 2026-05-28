# Dashboard - Sprint 5
**Gabriel Maldaner**

Render link:  
https://tripleten-6q1p.onrender.com

---

> Bibliotecas usadas:
> * Pandas
> * Streamlit
> * Plotly-Express

---

## Configuração Inicial UI Streamlit  
Usando `st.set_page_config()` para configurar parâmetros `page_title` e `layout` para ter o nome da aba customizado e o layout do dashboard ocupando a tela toda.  

Criação de 2 "colunas" para colocar os dois widgets disponíveis, usando `st.columns` e os parâmetros `[1,1]` (tamanho das colunas), `vertical_alignment` para alinhar ao topo, `border` para usar bordas entre os dois widgets e `width` para ocuparem a tela toda.

## Criação e configuração dos Widgets  
-  Widget 1  
\- Gráficos mostrados através de botões `st.button()` descrevendo cada opção.  
Ao apertar, retorna o `if` statement adequado para gerar o gráfico solicitado.    

- Widget 2  
\- Extraindo as colunas do `df.columns` usando `st.multiselect()` (para apresentar em forma de lista na UI) e alocando na variável `selected_cols`.  
\- Ao iterar sobre ela num `for loop`, conseguimos acessar cada coluna e retornar o comando de criação do gráfico de histograma baseado na escolha da coluna.  
\- No bloco `if - else`, há a distinção de colunas numéricas e categóricas para criação do Histograma, retornando um `st.warning()` para colunas categóricas.


## Gráficos disponíveis  
### Widget 1
- Histograma de `'odometer'`
- Dispersão de `'price'` vs `'odometer'`
- Dispersão de `'price'` vs `'model_year'`
- Barras de `'count'` vs `'transmission'`
- Barras de `'price'` vs `'transmission'`

### Widget 2
- Opções de Histogramas interativo em lista, com opções `['price', 'odometer', 'model_year']`
- Retorno de `st.warning()` para o restante das colunas:  
Achei interessante manter todas as colunas, mesmo sem utilizá-las, para um próximo widget.

## Configuração `config.toml`

Uso do seguinte bloco no arquivo `config.toml`, para configuração base da UI:

```toml
[theme]
primaryColor="#3B82F6"
backgroundColor="#0F172A"
secondaryBackgroundColor="#1E293B"
textColor="#F8FAFC"
font="sans serif"
```
