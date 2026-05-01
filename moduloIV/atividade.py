import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Análise do Preço do Ouro")

# carregar e tratar dados
df = pd.read_csv("data/gold_data.csv", skiprows=[1,2])
df.rename(columns={"Price": "Date"}, inplace=True)

df["Date"] = pd.to_datetime(df["Date"])
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
df["Volume"] = pd.to_numeric(df["Volume"], errors="coerce")

df = df.sort_values("Date")

# =========================
# 📈 1. GRÁFICO DE LINHA
# =========================
st.subheader("📈 Gráfico de Linha - Evolução do Preço")

st.line_chart(df.set_index("Date")["Close"])

st.write("👉 Mostra como o preço do ouro varia ao longo do tempo, permitindo identificar tendências.")

# =========================
# 📊 2. GRÁFICO DE BARRA
# =========================
st.subheader("📊 Gráfico de Barra - Volume por período")

df_bar = df.tail(10)  # últimos 10 dias

st.bar_chart(df_bar.set_index("Date")["Volume"])

st.write("👉 Compara valores entre períodos, facilitando ver dias com maior volume de negociações.")

# =========================
# 🔵 3. GRÁFICO DE DISPERSÃO
# =========================
st.subheader("🔵 Gráfico de Dispersão - Preço x Volume")

fig, ax = plt.subplots()
ax.scatter(df["Close"], df["Volume"])

ax.set_xlabel("Preço")
ax.set_ylabel("Volume")
ax.set_title("Relação entre preço e volume")

st.pyplot(fig)

st.write("👉 Mostra a relação entre duas variáveis. Aqui vemos se preços maiores estão associados a maior volume.")

# =========================
# 🥧 4. GRÁFICO DE PIZZA
# =========================
st.subheader("🥧 Gráfico de Pizza - Distribuição de Alta vs Baixa")

# criar categoria
df["Movimento"] = df["Close"].diff().apply(lambda x: "Alta" if x > 0 else "Baixa")

contagem = df["Movimento"].value_counts()

fig2, ax2 = plt.subplots()
ax2.pie(contagem, labels=contagem.index, autopct="%1.1f%%")

st.pyplot(fig2)

st.write("👉 Mostra a proporção de dias em que o preço subiu (Alta) ou caiu (Baixa).")

# =========================
# 📋 TABELA DE DADOS
# =========================
st.subheader("📋 Dados do Dataset")

st.dataframe(df)