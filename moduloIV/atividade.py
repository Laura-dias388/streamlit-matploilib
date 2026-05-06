import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title(" Análise do Preço do Ouro")

df = pd.read_csv("data/gold_data.csv", skiprows=[1,2])

df.rename(columns={"Price": "Date"}, inplace=True)

df["Date"] = pd.to_datetime(df["Date"])
df["Close"] = pd.to_numeric(df["Close"])
df["Volume"] = pd.to_numeric(df["Volume"])


df = df.sort_values("Date")
datas = sorted(df["Date"].dt.date.unique())

data_inicio = st.selectbox("Data inicial:", datas)
data_fim = st.selectbox("Data final:", datas, index=len(datas)-1)

df = df[(df["Date"].dt.date >= data_inicio) & (df["Date"].dt.date <= data_fim)]#condição para pegar o intervalo de datas
st.subheader(" Gráfico de Linha - Evolução do Preço")

st.line_chart(df.set_index("Date")["Close"])

st.write(" Mostra como o preço do ouro varia ao longo do tempo, permitindo identificar tendências.")

st.subheader(" Gráfico de Barra - Volume por período")

df_bar = df.tail(10)  

st.bar_chart(df_bar.set_index("Date")["Volume"])#grafico de barras

st.write(" Compara valores entre períodos, facilitando ver dias com maior volume de negociações.")

st.subheader(" Gráfico de Dispersão - Preço x Volume")

figure, ax = plt.subplots()
ax.scatter(df["Close"], df["Volume"])#grafico de dispersão

ax.set_xlabel("Preço")
ax.set_ylabel("Volume")
ax.set_title("Relação entre preço e volume")

st.pyplot(figure)

st.write(" Mostra a relação entre duas variáveis. Aqui vemos se preços maiores estão associados a maior volume.")

st.subheader(" Gráfico de Pizza - Distribuição de Alta vs Baixa")

df["Movimento"] = df["Close"].diff().apply(lambda x: "Alta" if x > 0 else "Baixa")#mostra se subiu ou caiu / diferença de valor e valor anterior

contagem = df["Movimento"].value_counts()#contagem de vezes em que um valor aparece

fig2, ax2 = plt.subplots()# Para criar o quadro e a tela
ax2.pie(contagem, labels=contagem.index)

st.pyplot(fig2)# exibindo o gráfico

st.write(" Mostra a proporção de dias em que o preço subiu (Alta) ou caiu (Baixa).")# escrever 

st.subheader(" Dados do Dataset")#subtitulo

st.dataframe(df)#exibindo os dados do dataset em formato de tabela