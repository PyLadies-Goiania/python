#!/usr/bin/env python
# coding: utf-8

# # PyLadies Goiânia - Brincando com Python 01 - 11/01/2020

# In[ ]:


print ('Hello World!')


# In[ ]:


"Hello World!"


# Comentários

# In[1]:


# Para fazer comentários no Python usamos #


# In[ ]:


# Para executar uma célula basta apertar CTRL + ENTER ou clicar sobre RUN


# Operações Matemáticas Simples:

# In[ ]:


# Adição


# In[ ]:


12 + 8 


# In[ ]:


# Subtração


# In[ ]:


24 - 17


# In[7]:


# Multiplicação


# In[ ]:


2 * 6


# In[ ]:


# Divisão


# In[ ]:


24 / 8


# In[ ]:


# Potenciação


# In[ ]:


2**3


# In[ ]:


# Radicação 


# In[ ]:


8**(1/3)


# Variáveis

# In[ ]:


# int ou números inteiros


# In[ ]:


# float ou ponto flutuante / números reais


# In[ ]:


# string ou sequência de caracteres


# In[ ]:


# Em Python não é necessário que você declare o tipo de variável irá utilizar.


# In[ ]:


A = 3


# In[ ]:


B = 3.2


# In[ ]:


C = 'Três'


# As operações com números float acontecem da mesma forma que com os números inteiros

# In[ ]:


8.2 + 1.7


# In[ ]:


9.3 - 2.8


# In[ ]:


5.6 * 7


# In[ ]:


4.9 / 3.1


# Strings

# In[ ]:


# As strings são delimintadas por aspas


# In[10]:


Pnome = 'Karen '


# In[11]:


Unome = 'Pessoa'


# In[12]:


print (Pnome, Unome)


# In[ ]:


Cnome = Pnome + Unome
print (Cnome)


# In[19]:


# Para 'pular uma linha' você pode usar o comando \n após a última palavra da linha


# In[ ]:


# Agora se quiser apenas organizar em colunas, utilizeu o comando \t após a última palavra da coluna


# In[ ]:


Chamada = 'Alunas \t Palestra \t P/F'


# In[ ]:


Chamada_2 = 'Karen \n Michelly \n Gabriella \n Chris \n Sâmela \n Érika'
print (Chamada_2)


# Algumas funções do Pythob

# In[ ]:


# A função type nos informa qual o tipo de variável estamos trabalhando


# In[ ]:


type(A)


# In[ ]:


type(B)


# In[ ]:


type(C)


# In[ ]:


# Ainda temos as funções de conversão, que modificam o tipo de variável a ser trabalhada 


# In[ ]:


int(3.5)


# In[ ]:


float(6)


# In[ ]:


str(8)


# In[ ]:


# A função round nos ajuda no arredondamento de valores


# In[ ]:


round(2.964875)


# In[ ]:


round(2.964875, 3)


# Trabalhando com variáveis

# In[ ]:


varA = 1


# In[ ]:


varB = 2


# In[ ]:


varC = 3


# In[ ]:


varA


# In[ ]:


type(varA)


# In[ ]:


varA + varB


# In[ ]:


# Reatribuindo valor a uma variável


# In[ ]:


varC = 'Arroz'


# In[ ]:


resultado = varA * 10


# In[ ]:


resultado


# In[ ]:


resultado_1 = varB / 4


# In[ ]:


resultado_1


# In[ ]:


# Declarando vários valores a variáveis


# In[ ]:


variavel1, variavel2 = 1, 'Teste'


# In[ ]:


variavel1


# In[ ]:


variavel2


# In[ ]:


# Restrições para criação de variáveis


# In[ ]:


# Não podemos iniciar o nome de uma nova variável com um número


# In[ ]:


# Nâo podemos nomear variáveis com palavras reservadas (palavras de funções, por exemplo)


# Trabalhando com Strings

# In[ ]:


frase = 'Python eh uma linguagem sensacional'


# In[ ]:


frase


# In[ ]:


# Indexando Strings


# In[ ]:


# IMPORTANTE: Observe que em Python o índice começa com 0


# In[ ]:


frase[0]


# In[ ]:


frase[8]


# In[ ]:


# O Python não permite substituição de caracteres em strings


# In[ ]:


frase[0] = 'R'


# In[ ]:


# Slicing: percorrendo o string


# In[ ]:


frase[0:6]


# In[ ]:


frase[6:]


# In[ ]:


frase[:6]


# In[ ]:


# Concatenando strings


# In[ ]:


frase1 = 'Lugar de mulher eh '


# In[ ]:


frase2 = 'onde ela quiser'


# In[ ]:


frase1 + frase2


# In[ ]:


# Observe que para Strings não é possível realizar operações matemáticas
# Aqui o sinal de + é entendido como uma concatenação
# Similarmente, o sinal de * é entendido como uma repetição


# In[ ]:


Cnome * 2


# In[ ]:


# Objetos String - Métodos


# In[ ]:


# Em Python, strings são objetos e a eles cabem alguns métodos que podem ser aplicados


# In[ ]:


frase = 'PyLadies eh a melhor comunidade de Python voltada para as mulheres'


# In[ ]:


# Contagem de palavras
frase.count('PyLadies')


# In[ ]:


# A função lower / upper / capitalize


# In[ ]:


frase.lower()


# In[ ]:


frase.upper()


# In[ ]:


frase.capitalize()


# In[ ]:


# Teste para lower / upper / capitalize. Responde Falso ou Verdadeiro


# In[ ]:


frase.islower()


# In[ ]:


# A função split quebra uma frase em uma lista de termos


# In[ ]:


frase.split()


# In[ ]:


frase.split('de')


# In[ ]:




