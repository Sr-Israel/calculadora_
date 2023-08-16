# Função de soma
def soma(a, b):
    return a + b

# Função de subtração
def subtracao(a, b):
    return a - b

# Função de multiplicação
def multiplicacao(a, b):
    return a * b

# Função de divisão
def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por zero."
    else:
        return a / b

# Menu da calculadora
print("Escolha uma opção:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite sua opção (1/2/3/4): "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == 1:
    print(num1, "+", num2, "=", soma(num1, num2))

elif opcao == 2:
    print(num1, "-", num2, "=", subtracao(num1, num2))

elif opcao == 3:
    print(num1, "*", num2, "=", multiplicacao(num1, num2))

elif opcao == 4:
    print(num1, "/", num2, "=", divisao(num1, num2))

else:
    print("Opção inválida! Por favor escolha uma opção válida.")