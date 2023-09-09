# Peça ao usuário para inserir dois números e uma operação (+, -, *, /).
# Realize a operação e exiba o resultado.

print ("------------Calculadora Simples------------")
print ()
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
operacao = input("Escolha uma operação (+, -, *, /) ")

print ()

if operacao == "+":
    print(f"O resultado é {num1 + num2}")
elif operacao == "-":
    print(f"O resultado é {num1 - num2}")
elif operacao == "*":
    print(f"O resultado é {num1 * num2}")
elif operacao == "/":
    print(f"O resultado é {num1 / num2}")