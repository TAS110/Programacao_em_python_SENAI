#1
numero = int(input("Digite um número: "))

match numero % 2:
    case 0: 
        print("O número é par.")
    case _: 
        print("O número é ímpar.")
#2
numero = float(input("Digite um número: "))

match numero:
    case _ if numero > 0: 
        print("O número é positivo.")
    case _ if numero < 0: 
        print("O número é negativo.")
    case _: 
        print("O número é zero.")

#3
texto = input("Digite um texto: ")

match texto.strip():
    case "": 
        print("A string está vazia.")
    case _: 
        print("A string não está vazia.")

#4
        numero = float(input("Digite um número: "))

match numero:
    case _ if numero > 10: 
        print("O número é maior que 10.")
    case _ if numero < 10: 
        print("O número é menor que 10.")
    case _: 
        print("O número é igual a 10.")


#5
idade = int(input("Digite a idade: "))

match idade:
    case _ if idade <= 12: 
        print("Criança")
    case _ if idade <= 17: 
        print("Adolescente")
    case _ if idade <= 35: 
        print("Jovem")
    case _ if idade <= 64: 
        print("Adulto")
    case _ if idade <= 78:
        print("Idoso")
