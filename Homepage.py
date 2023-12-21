import streamlit as st

#Título e ícone
st.set_page_config(
    page_title="Site Python",
    page_icon=":nerd_face:"
)

# Cria uma sidebar que utiliza a pasta pages
st.sidebar.success("Selecione uma página acima.")

# Header 
st.title("1. Introdução à Programação e Python: ")
st.divider()
st.header("O que é programação?")

st.header("Por que aprender Python?")
st.header("Como instalar Python no seu computador.")
