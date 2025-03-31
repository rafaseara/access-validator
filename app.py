import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api/verificar_acesso/"

st.set_page_config(page_title="Validador de Acessos", layout="centered")
st.title("Verificando o Acesso")

nome_usuario = st.text_input("Insira seu nome: ")
lugar_usuario = st.text_input("Insira a área que quer entrar: ")
