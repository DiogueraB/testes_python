# Peça ao usuário para inserir seu salário e o tempo de serviço. Se o tempo de serviço
# for superior a 5 anos, conceda um bônus de 5% ao salário.

print ("--------------Bonus Salarial--------------")
print ()

salario = float(input ("Insira seu salário: "))
tempo = int(input ("Qual é o seu tempo de serviço: "))

total = 0
if tempo > 5:
    total = salario * 1.05
else:
    total = salario

if total > salario:
    print (f"Seu novo salário é de {total}")
else:
    print (f"Seu salário permanece o mesmo")

