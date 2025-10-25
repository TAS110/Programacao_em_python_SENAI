## 1 - Crie um programa para efetuar a leitura de 
# um número inteiro e apresentar o resultado do 
# quadrado deste número.

n = int(input('>>'))
quadrado =  n ** 2
print(quadrado)



## 2 - Crie duas variáveis para armazenar 
# seu primeiro nome e sobrenome. Em seguida, 
# concatene-as para formar seu nome completo 
# e exiba o resultado.

nome = 'Beatriz'
sobrenome = 'Alves'
print(nome, sobrenome)

## 3 - Peça ao usuário para digitar dois 
# números inteiros e armazene-os em variáveis. 
# Realize a concatenação desses números como 
# strings e exiba o resultado.

n1  =  int(input('Digite 1 numero inteiro'))
n2  =  int(input('Digite o 2º numero inteiro'))
print(str(n1),str(n2))

n1_str = str(n1)
n2_str = str(n2)
print(n1_str,n2_str)




## 4 - Crie uma variável para armazenar 
# a palavra "Python". Em seguida, adicione 
# um número inteiro ao final da palavra usando 
# a concatenação e exiba o resultado.

palavra  =  'Python'
n = 10
print(palavra,10)


## 5 - Declare uma variável contendo uma 
# frase. Em seguida, peça ao usuário para 
# digitar uma palavra e concatene essa 
# palavra no final da frase. Exiba o resultado.

frase  =  'minha comida favorita é'
comida = input('Digite uma comida: ')
print(frase, comida)