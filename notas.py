# Peça ao usuário para inserir uma nota de 0 a 100 e, em seguida, classifique-a como
# "A" (90-100), "B" (80-89), "C" (70-79), "D" (60-69) ou "F" (abaixo de 60).

print ("---------------Classificação de Notas---------------")
print ()

nota = int(input("Insira uma nota de 0 a 100: "))

if nota >= 90 and nota <= 100:
    print ("Sua nota é : A")
elif nota >= 80 and nota <= 89:
    print ("Sua nota é: B ")
elif nota >= 70 and nota <= 79:
    print ("Sua nota é: C ")
elif nota >= 60 and nota <= 69:
    print ("Sua nota é: D ")
elif nota <= 60:
    print ("Sua nota é: F ")