#1
def comparar_numeros(num1, num2):
    resultado1 = "Par" if num1 % 2 == 0 else "Ímpar"
    resultado2 = "Par" if num2 % 2 == 0 else "Ímpar"
    print(f"O primeiro número ({num1}) é {resultado1}")
    print(f"O segundo número ({num2}) é {resultado2}")

comparar_numeros(5, 8)

#2
def multiplicar_tres(num1, num2, num3):
    resultado = num1 * num2 * num3
    return resultado

print(multiplicar_tres(2, 3, 4))  

#3
def elevar_numero(base, expoente):
    resultado = base ** expoente
    return resultado

print(elevar_numero(2, 5)) 

#4
def verificar_idade(idade):
    if idade == 18:
        print("Parabéns! Você acabou de atingir a maioridade.")
    else:
        print("Você ainda não tem 18 anos ou já passou dessa idade.")

verificar_idade(18)

#5
def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    return idade

print(calcular_idade(2005, 2025)) 


#6
def brasil_ganhou_copa_1999():
    copa_1999 = "Brasil"
    vencedor = "Brasil"  
    if vencedor == copa_1999:
        return True
    else:
        return False
if brasil_ganhou_copa_1999():
    print("Sim, o Brasil ganhou a Copa de 1999!")
else:
    print("Não, o Brasil não ganhou a Copa de 1999.")

#7
#-1
def cumprimentar_cliente():
    print("Bem-vindo ao nosso restaurante!")
#-2
def restaurante():
    menu = ["Salada", "Macarronada", "Sanduíche", "Sorvete"]
    print("Nosso cardápio:")
    for i, item in enumerate(menu, start=1):
        print(f"{i} - {item}")
    
    escolha = int(input("Escolha o número do seu prato: "))
    if 1 <= escolha <= len(menu):
        print(f"Você escolheu {menu[escolha - 1]}. Bom apetite!")
    else:
        print("Escolha inválida!")
cumprimentar_cliente()
restaurante()
