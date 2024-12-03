import math

try:
    nu01 = int(input("Insira um número inteiro: "))
    nu02 = int(input("Insira mais um número inteiro: "))
    resultado = nu01 // nu02
    print(f"O resultado da divisão é = {resultado}")
except:
    print("Esse número não pode ser dividido")
else:
    print("espero ter ajudado")
finally:
    print("O importante é participar!")



# # # area do circulo
raio_circulo = float(input("Digite o raio do circulo:"))
area = math.pi * raio_circulo ** 2 # ** 2 - referece ao quadrado
print(f"{area:.2f}") #format para pegar só as duas casas decimais depois do "."



# #digite uma fata no formato "dd/mm/aaaa" e imprima o dia, mês e ano 
data = input("Insira uma data no formato dd/mm/aaa: ")
list_data_separada = data.split("/")
print(f"O dia é : {list_data_separada[0]}")
print(f"O mês é : {list_data_separada[1]}")
print(f"O ano é : {list_data_separada[2]}")



#verificar o númeor é um interio
numero = input("Insira um número: ")
if numero.isdigit():  # Verifica se a entrada consiste apenas em dígitos
    print("O número é um inteiro.")
else:
    print("O número não é um inteiro.")  # Se não for, informa que não é um inteiro



#calculadora simples
def calcular():
    print("Bem-vindo à calculadora!")
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    # Solicitar escolha do usuário
    escolha = input("Digite o número da operação (1/2/3/4): ")

    # Solicitar números ao usuário
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))

    if escolha == '1':
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")

    elif escolha == '2':
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")

    elif escolha == '3':
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")

    elif escolha == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
        else:
            print("Erro! Divisão por zero não é permitida.")

    else:
        print("Opção inválida.")

# Chamar a função da calculadora
calcular()

