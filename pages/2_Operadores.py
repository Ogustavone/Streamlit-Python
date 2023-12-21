import streamlit as st

st.title("Operadores em Python:")
st.sidebar.markdown("# Operadores")

st.divider()

st.write('Em Python, os operadores são símbolos especiais fundamentais para realizar operações em valores e variáveis.')
st.write('Eles são essenciais para manipular dados de maneira eficaz, permitindo a realização de operações lógicas, aritméticas e de comparação.')

st.write('Algumas das ações que podemos realizar usando operadores são')

st.write('')
st.subheader('Comparar informações')

code1='nome = "Lucas"\n\nif nome != "Luan":\n   print("Quem é " + nome + "?")'
st.code(code1, language="python")

st.subheader('Realizar cálculos')

code2='print("O dobro de 40 é:", 40 * 2)\nprint("2 elevado à potência de 3 é:", 2 ** 3)'
st.code(code2, language="python")

st.subheader('Fazer uma operação lógica')

code3='valor_1 = 98\nvalor_2 = 60\n\n# Verifica se um dos valores é menor ou igual a 100\nif valor_1 <= 100 or valor_2 <= 100'
st.code(code3, language='python')


st.write('Em programação, operadores são fundamentais para realizar operações lógicas,  \naritméticas e comparação, permitindo que os programadores manipulem dados de maneira eficaz.')

st.divider()

st.header('Operadores aritméticos') # Header 
st.caption('Nesta página, exploraremos os operadores aritméticos em Python usando as variáveis a e b como exemplos.')

code4='a = 5\nb = 2'
st.code(code4, language='python')

st.subheader('Adição (+)') # Sub 1

code5='print("Para realizar adições, utilize +")\n\nsoma = a + b #7'
st.code(code5, language='python')

st.subheader('Subtração (-)') # Sub 2

code6='print("Para subtrações, utilize -")\nsubtracao = a - b # 3'
st.code(code6, language='python')

st.subheader('Divisão') # Sub 3

code7='print("Aqui temos uma divisão que utiliza uma barra /")\ndivisao = a / b  # 2.5\n\nprint("Para fazer essa divisão inteira, use barras duplas //")\ndivisao_inteira = a // b # 2\n\nprint("Para porcentagens ou resto, %")\nporcentagem = a % b # 1'
st.code(code7, language='python')

st.subheader('Multiplicação') # Sub 4

code8='print("Para multiplicações simples, use *")\nmultiplicacao = a * b  # 10\n\nprint("Para elevar um número ao outro, **")\npotencia = a ** b  # 25'

st.code(code8, language='python')

st.subheader('Exemplo de uso composto') # Sub 3

code9='print("Expressão aritmética composta: (a + b) * 2")\nexpressao_composta = (a + b) * 2'
st.code(code9, language='python')

st.write("")
st.write("Estes operadores são ferramentas poderosas que possibilitam realizar uma variedade de cálculos e manipular dados.  \n\nAo compreendê-los, você estará mais preparado para resolver problemas e desenvolver algoritmos eficientes.")

st.divider()

st.header('Operadores de Comparação')
st.write('Os operadores de comparação são utilizados para comparar valores e expressões, retornando valores booleanos (Verdadeiro ou Falso) como resultado.')

st.subheader('Maior que (>)') #Sub 1
code10='print("Para verificar se um valor é maior que outro, utilize o operador >")\nmaior_que = 5 > 3  # Verdadeiro, pois 5 é maior que 3'
st.code(code10, language='python')

st.subheader('Menor que (<)') #Sub 2
code11='print("Para verificar se um valor é menor que outro, utilize o operador <")\nmenor_que = 2 < 4  # Verdadeiro, pois 2 é menor que 4'
st.code(code11, language='python')

st.subheader('Igual a (==)') #Sub 3
code12='print("Para verificar se dois valores são iguais, utilize o operador ==")\nigual_a = 7 == 7  # Verdadeiro, pois 7 é igual a 7'
st.code(code12, language='python')

st.subheader('Diferente de (!=)') #Sub 4
code13='print("Para verificar se dois valores são diferentes, utilize o operador !=")\ndiferente_de = 10 != 5  # Verdadeiro, pois 10 é diferente de 5'
st.code(code13, language='python')

st.subheader('Maior ou Igual a (>=)') #Sub 5
code14='print("Para verificar se um valor é maior ou igual a outro, utilize o operador >=")\nmaior_ou_igual = 8 >= 8  # Verdadeiro, pois 8 é igual a 8'
st.code(code14, language='python')

st.subheader('Menor ou Igual a (<=)') #Sub 6
code15='print("Para verificar se um valor é maior ou igual a outro, utilize o operador >=")\nmaior_ou_igual = 8 >= 8  # Verdadeiro, pois 8 é igual a 8'
st.code(code15, language='python')


st.write('#### Ainda há outros tipos de comparadores, veremos eles mais para frente...  \n\nÉ importante lembrar que: esses valores não valem apenas para dados relacionados à números')