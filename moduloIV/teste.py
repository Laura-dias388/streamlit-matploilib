import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Distribuição Normal Interativa 📊")

# 🔧 sliders interativos
mu = st.slider("Valor de μ (média)", 0.0, 16.0, 8.0)
sigma = st.slider("Valor de σ (desvio padrão)", 0.1, 5.0, 2.0)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# 🔹 gráfico 1 (ruído suavizado)
np.random.seed(19680801)
s = 2.9 * np.convolve(np.random.randn(500), np.ones(30) / 30, mode='valid')
ax1.plot(s)
ax1.axhspan(-1, 1, alpha=0.1)
ax1.set(ylim=(-1.5, 1.5), title="Sinal com Ruído")

# 🔹 gráfico 2 (distribuição normal)
x = np.linspace(0, 16, 401)
y = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

ax2.axvspan(mu - 2*sigma, mu - sigma, color='0.95')
ax2.axvspan(mu - sigma, mu + sigma, color='0.9')
ax2.axvspan(mu + sigma, mu + 2*sigma, color='0.95')
ax2.axvline(mu, color='darkgrey', linestyle='--')

ax2.plot(x, y)
ax2.set(title="Distribuição Normal")

# 👇 renderiza no Streamlit
st.pyplot(fig)