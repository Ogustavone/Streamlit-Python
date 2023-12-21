import streamlit as st

st.title("Variáveis e tipos de Dados: ")
st.sidebar.markdown("# Variáveis e dados")

st.divider()

st.header("O que são variáveis? ")      # Header 1
st.caption("Variável em Python é como uma :red[caixa]...")

st.write("Imagine que você tem uma caixa onde pode colocar alguma coisa,  \nessa coisa pode ser um :green[número], uma :green[palavra] ou qualquer outra informação...")

code1="idade = 20 # Essa é uma variável idade, onde seu valor é 20\n nome = 'matheus' # Essa é uma variável nome, seu valor é o texto: Matheus"
st.code(code1, language='python')

st.write("Uma das formas de utilizar o valor obtido na variável é :blue[mostrar isso na tela].")

code2='print(idade)\nprint(nome)\n# Esse comando "imprime" algo na tela! '
st.code(code2, language='python')

st.write("Em Python, você pode usar variáveis para armazenar diferentes tipos   \nde informações: números, palavras ou até mesmo se algo é verdadeiro ou falso.   \n  \nAs variáveis são como as caixas que ajudam o computador a armazenar as coisas...")

st.divider()

st.header("Tipos de dados em Python")   # Header 2
st.caption('Abaixo estão alguns tipos de dados que podemos :red[armazenar] ao programar em Python.')


st.subheader("1 - Números inteiros (:green[int])")      # Sub-1
st.write('Representa um número inteiro, sem parte decimal ou "quebrada".')

code3 = 'int # Curiosidade: Isso pode ser usado para transformar algo em número inteiro \n\nvalor = 10'
st.code(code3, language='python')

st.write('Valores inteiros são lidos pelo Python como um valor :green[int].')


st.subheader("2 - Números flutuantes (:green[float])")  # Sub-2
st.write('Representa números com casas decimais.')

code4 = 'float # Isso também pode transformar algo em float \n \nvalor_decimal = 15.59'
st.code(code4, language='python')

st.write('Valores decimais são lidos como um valor :green[float].')


st.subheader("3 - Strings (:green[str])")               # Sub-3
st.write('Uma string representa um texto ou qualquer sequência de caracteres.')

code5 = 'str # Usar isso transforma um valor em caractere \n \nstring = "Marcelo"'
st.code(code5, language='python')

st.write('Strings são lidos como caracteres do tipo :green[str].')


st.subheader("4 - Valor Booleano (:green[bool])")       # Sub-4
st.write('Um valor que representa valores lógicos, como verdadeiro(:blue[true]) e falso(:red[false]).')

code6 = 'bool # isso define algo como valor booleano\n\nvalor_booleano=True # Também pode usar False\n\n\nresposta = (19>20) # Compara 2 números e retorna um valor booleano.'
st.code(code6, language='python')

st.write('Geralmente é utilizado em expressões condicionais.')
st.caption("Todos esses tipos de dados podem ser utilizados como valores dentro das variáveis.")
st.divider()

st.header("Estrutura do código")        # Header 3
st.caption('Quando você estiver montando um programa, preste :red[atenção] na estrutura utilizada,  \npois o interpretador sempre seguirá uma ordem na leitura do código do início ao fim')

code7='idade = 20\nnome = "João"\ncor_favorita = "Amarelo"\nidade = 13\n\nprint("Nome:", nome)\nprint("Cor favorita:", cor_favorita)\nprint ("Idade:", idade)\n\n# Você pode rodar isso em seu interpretador Python.'
st.code(code7, language='python')

st.write('Ao rodar este código, você pode perceber que a idade que aparece na tela sempre será a última,  \npois o programa apenas :blue[substituiu a informação] que estava armazenada pela mais atual.')

st.write('Portanto, ao montar a :blue[lógica] do seu programa, pense com atenção nos passos que ele precisa seguir,  \nporque uma pequena mudança de ordem na estrutura pode ser muito significativo para o funcionamento!')