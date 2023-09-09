# Crie um programa que peça ao usuário para inserir sua idade e, em
# seguida, informe se a pessoa é menor de idade ou maior de idade.

print ("--------------Verificação de Idade--------------")
print ()
idade = int(input("Qual sua idade?  "))

if idade < 18:
    print("Você é menor de idade")
elif idade >= 18:
    print("Você é maior de idade")
