import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Análise do Preço do Ouro")
#nformações diárias do preço do ouro, incluindo valores de abertura, fechamento, máxima, mínima e volume de negociações

# lendo CSV
df = pd.read_csv("data/gold_data.csv", skiprows=[1,2])#limpando linhas inúteis 

# nome da coluna
df.rename(columns={"Price": "Date"}, inplace=True)#renomeei price para data

# convertendo a data
df["Date"] = pd.to_datetime(df["Date"])


datas = sorted(df["Date"].dt.date.unique())#removendo hora e datas repetidas
data_inicio = st.selectbox("Data inicial:", datas)
data_fim = st.selectbox("Data final:", datas, index=len(datas)-1)

df_filtro = df[(df["Date"].dt.date >= data_inicio) & (df["Date"].dt.date <= data_fim)]


st.subheader("Gráfico de Linha")
st.line_chart(df_filtro.set_index("Date")["Close"])#grafico de linha


st.subheader("Gráfico de Barra")
st.bar_chart(df_filtro.tail(10).set_index("Date")["Volume"])#barra


st.subheader("Dispersão")

fig, ax = plt.subplots()
ax.scatter(df_filtro["Close"], df_filtro["Volume"])
st.pyplot(fig)


st.subheader("Pizza")

mov = df_filtro["Close"].diff()

contagem = mov.apply(lambda x: "Alta" if x > 0 else "Baixa").value_counts()

fig2, ax2 = plt.subplots()
ax2.pie(contagem, labels=contagem.index)
st.pyplot(fig2)


st.subheader("Dados")
st.dataframe(df_filtro)