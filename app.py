import streamlit as st
import requests

API_URL = "https://access-validator-production.up.railway.app/api/verificar_acesso"

st.set_page_config(page_title="Validador de Acessos", layout="centered")
st.title("Verificando o Acesso")

nome_usuario = st.text_input("Insira seu nome: ")
lugar_usuario = st.text_input("Insira a área que quer entrar: ")

def verificando_acesso():
    if not nome_usuario or not lugar_usuario:
        st.text("Por favor, preencha ambos os campos")
        return

    try:
        response = requests.get(API_URL, params={"nome": nome_usuario, "lugar_acesso": lugar_usuario})
        if response.status_code == 200:
            st.success(response.json().get("mensagem", "Erro na resposta da API"))
        else:
            st.error("Erro ao conectar com a API.")
    except Exception as erro:
        st.error(f"Erro na conexão com a API: {erro}")

st.button("Acessar", on_click=verificando_acesso)