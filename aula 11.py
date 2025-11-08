#1
try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou o número {numero}.")
except ValueError:
    print("Erro: isso não é um número inteiro!")
    
#2
try:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    resultado = n1 / n2
    print(f"O resultado da divisão é: {resultado}")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero!")
except ValueError:
    print("Erro: digite apenas números válidos!")
    
#3

    list = [10, 20, 30, 40, 50]

    print("Lista disponível:", list)

try:
    indice = int(input("Digite o índice que deseja acessar (de 0 a 4): "))
    valor = list[indice]
    print(f"O valor no índice {indice} é: {valor}")
except IndexError:
    print("Erro: o índice digitado não existe na lista! Tente um número entre 0 e 4.")
except ValueError:
    print("Erro: digite apenas números inteiros!")
else:
    print("Acesso realizado com sucesso!")
finally:
    print("Programa finalizado.")