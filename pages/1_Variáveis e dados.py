import streamlit as st

st.title("Variáveis e tipos de Dados: ")
st.sidebar.markdown("# Variáveis e dados")

st.divider()

st.header("O que são variáveis? ") # Header 1
st.caption("Variável em Python é como uma :red[caixa]...")

st.write("Imagine que você tem uma caixa onde pode colocar alguma coisa,  \nessa coisa pode ser um número, uma palavra ou qualquer outra informação...")

code1="idade = 20 # Essa é uma variável idade, onde seu valor é 20\n nome = 'matheus' # Essa é uma variável nome, seu valor é o texto: Matheus"
st.code(code1, language='python')

st.write("Uma das formas de utilizar o valor obtido na variável é :blue[mostrar isso na tela].")

code2='print(idade)\nprint(nome)\n# Esse comando "imprime" algo na tela! '
st.code(code2, language='python')

st.divider()

st.write("Em Python, você pode usar variáveis para armazenar diferentes tipos   \nde informações: números, palavras ou até mesmo se algo é verdadeiro ou falso.   \n  \nAs variáveis são como as caixas que ajudam o computador a armazenar as coisas...")

st.header("Tipos de dados em Python") # Header 2
st.header("Estrutura do código") # Header 3