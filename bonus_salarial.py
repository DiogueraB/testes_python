# Peça ao usuário para inserir seu salário e o tempo de serviço. Se o tempo de serviço
# for superior a 5 anos, conceda um bônus de 5% ao salário.

print ("--------------Bonus Salarial--------------")
print ()

salario = float(input ("Insira seu salário: "))
tempo = int(input ("Qual é o seu tempo de serviço: "))

print ()

bonus = salario/1.05

if tempo > 5:
    print("Você recebeu um bônus de 5%")
    print (f"Seu salário atual é de {bonus + salario: .2f}")
else:
    print ("Você não pode receber bônus salarial")
    

