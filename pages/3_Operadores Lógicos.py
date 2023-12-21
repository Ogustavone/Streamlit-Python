import streamlit as st

st.title("Operadores Lógicos")
st.sidebar.markdown("# Op. lógicos")

st.divider()

st.write('Os operadores lógicos são utilizados para realizar operações de lógica booleana, combinando ou invertendo valores booleanos.')

st.subheader('And (E)')
code1='print("Para realizar a operação de E lógico, utilize o operador and")\np = True\nq = False\n\nresultado_and = p and q  # Falso, pois ambos os valores precisam ser verdadeiros'
st.code(code1, language='python')

st.subheader('Or (OU)')
code2='print("Para realizar a operação de OU lógico, utilize o operador or")\n\nresultado_or = p or q  # Verdadeiro, pois pelo menos um dos valores precisa ser verdadeiro'
st.code(code2, language='python')

st.subheader('Not (Negação)')
code3='print("Para realizar a operação de negação lógica, utilize o operador not")\n\nresultado_not = not p  # Falso, pois inverte o valor booleano de p'
st.code(code3, language='python')

st.divider()

st.header('Operadores Adicionais de Lógica/comparação')
st.caption('Não é necessário prender-se ao conteúdo de operadores adicionais no momento, mas é um conhecimento adicional no momento.')

st.subheader('in (pertence a...)') # Subheader
code4='print("Para verificar se um valor está presente em uma sequência, utilize o operador in")\nlista = [1, 2, 3, 4]\n\npertence = 3 in lista  # Verdadeiro, pois 3 está na lista'
st.code(code4, language='python')

st.subheader('not in (não pertence)') # Subheader
code5='print("Para verificar se um valor não está presente em uma sequência, utilize o operador not in")\n\nao_pertence = 6 not in lista  # Verdadeiro, pois 6 não está na lista'
st.code(code5, language='python')

st.subheader('is (mesmo objeto)') # Subheader
code6='print("Para verificar se dois objetos são o mesmo objeto em memória, utilize o operador is")\nobjeto_1 = [1, 2, 3]\nobjeto_2 = objeto_1\n\nmesmo_objeto = objeto_1 is objeto_2  # Verdadeiro, pois ambos referenciam o mesmo objeto em memória'
st.code(code6, language='python')

st.subheader('is not (objeto diferente)') # Subheader
code7='print("Para verificar se dois objetos não são o mesmo objeto em memória, utilize o operador is not")\noutro_objeto = [1, 2, 3]\n\nnao_mesmo_objeto = objeto_1 is not outro_objeto  # Verdadeiro, pois são objetos diferentes em memória'
st.code(code7, language='python')
