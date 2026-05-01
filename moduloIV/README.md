# 📊 Dashboard de Análise de Dados com Streamlit

Este projeto consiste no desenvolvimento de um dashboard interativo utilizando Python e a biblioteca Streamlit para análise e visualização de dados.

A aplicação foi construída com base em um dataset obtido do Kaggle, com foco em análise exploratória e apresentação visual das informações.

---

## 🎯 Objetivo

Desenvolver um dashboard que permita:

- Visualizar dados de forma interativa
- Aplicar filtros dinâmicos
- Gerar gráficos para análise
- Apresentar informações de forma clara e organizada

---

## 📁 Dataset

O dataset utilizado refere-se a dados históricos do preço do ouro, contendo informações como:

- Data
- Preço de fechamento (Close)
- Volume
- Máximo e mínimo

---

## 🛠️ Tecnologias utilizadas

- Python
- Pandas
- Streamlit
- Matplotlib

---

## ⚙️ Funcionalidades implementadas

### 📈 Gráfico de Linha
Mostra a evolução do preço do ouro ao longo do tempo, permitindo identificar tendências de crescimento ou queda.

---

### 📊 Gráfico de Barra
Apresenta a comparação do volume de negociações em diferentes períodos, facilitando a análise de variações.

---

### 🔵 Gráfico de Dispersão
Demonstra a relação entre o preço e o volume, permitindo observar possíveis correlações entre essas variáveis.

---

### 🥧 Gráfico de Pizza
Mostra a proporção de dias em que o preço do ouro teve alta ou baixa, facilitando a análise percentual.

---

### 📋 Tabela de Dados
Os dados do dataset são exibidos em formato de tabela interativa utilizando `st.dataframe()`, permitindo melhor visualização e exploração dos dados.

---

### 📅 Tratamento de Datas
A coluna de datas foi convertida para o formato `datetime` do Python, possibilitando ordenação e manipulação temporal.

---

### 🎛️ Filtro Interativo
Foi implementado um filtro utilizando `selectbox` para selecionar períodos específicos e variar as informações exibidas nos gráficos.

---

## 🧠 Metodologia

1. Escolha do dataset no Kaggle  
2. Importação do arquivo CSV  
3. Tratamento e limpeza dos dados  
4. Conversão de tipos (especialmente datas)  
5. Criação dos gráficos  
6. Construção do dashboard com Streamlit  
7. Implementação de filtros interativos  

---

## ▶️ Como executar o projeto

### Pré-requisitos:
- Python instalado
- Ambiente virtual (.venv)

---

### Passos:

```bash
# ativar ambiente virtual
source .venv/Scripts/activate

# acessar pasta do projeto
cd moduloIV

# rodar aplicação
streamlit run teste2.py