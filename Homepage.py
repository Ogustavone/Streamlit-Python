import streamlit as st

#Título e ícone
st.set_page_config(
    page_title="Site Python",
    page_icon=":nerd_face:"
)

# Cria uma sidebar que utiliza a pasta pages
st.sidebar.success("Selecione uma página acima.")

# Título
st.title("1. Introdução à Programação e Python: ")

st.divider()

st.image('images/python.jpg', caption='<Disponível em: https://apexensino.com.br/voce-conhece-a-linguagem-python/ Acesso em: 21/12/2023>')

st.header("O que é programação?") # Header 1

st.write("Programação é a arte de criar instruções para computadores executarem tarefas específicas.  \nConsiste em desenvolver algoritmos e traduzí-los para que o computador possa entender e executar.  \n\nA programação é fundamental para criar softwares, aplicativos e sistemas que impulsionam a tecnologia moderna e suas necessidades.")


st.header("Por que aprender Python?") # Header 2

st.write("Python é uma linguagem de programação versátil, poderosa e de fácil aprendizado.  \nSuas características incluem uma sintaxe clara e legível, o que facilita a compreensão para iniciantes. \n\nAlém disso, é amplamente utilizado em diversas áreas, como desenvolvimento web, inteligência artificial, ciência de dados e automação. A comunidade Python é robusta, oferecendo suporte e recursos valiosos.")

st.header("Como instalar Python no seu computador.") # Header 3

# Passo 1
st.subheader("1. Acesse o Site Oficial:")
st.write("Visite o site oficial do Python em [python.org](https://www.python.org/).")

# Passo 2
st.subheader("2. Download do Python:")
st.write("No site, vá para a seção de downloads e escolha a versão mais recente do Python para o seu sistema operacional (Windows, macOS, ou Linux).")

# Passo 3
st.subheader("3. Instalação:")
st.write("Execute o instalador baixado e siga as instruções. Certifique-se de marcar a opção 'Adicionar Python ao PATH' durante a instalação.")

# Passo 4
st.subheader("4. Verificação da Instalação:")
st.write("Abra o terminal (ou prompt de comando) e digite `python --version` ou `python -V`. Se a instalação foi bem-sucedida, você verá a versão do Python instalada.")