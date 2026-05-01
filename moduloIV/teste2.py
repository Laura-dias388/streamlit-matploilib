import streamlit as st

st.title("Meu primeiro app com Streamlit 🚀")

st.write("Ao infinito e além!")

nome = st.text_input("Digite seu nome:")

if nome:
    st.success(f"Olá, {nome}! 👋")
# nome = st.text_input("Digite seu nome!") 
# if nome:
#   st.write(f"Olá, {nome}!!")