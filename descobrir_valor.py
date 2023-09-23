## Exercício 3 - Jogo de Descobrir o Valor
# - Programa que sorteia um valor de 1 a 100.
# - Programa informará se o chute é menor ou maior que o valor sorteado.
# - O processo se repete até que o jogador acerte o valor sorteado.

from random import randint

valorsorteado = randint(0 , 100)
tentativa = 0

escolha = int(input("Escolha um número: "))

while escolha != valorsorteado:

    if escolha > valorsorteado:
        print ("O valor sorteado é menor")     
        print()
    else:
        print ("O valor sorteado é maior")
        print()
        
    escolha = int(input("Escolha um número: "))
    tentativa += 1

if escolha == valorsorteado:
    print()
    print("Você acertou !!!")
    print(f"Para acertar foram necessárias {tentativa} tentativas")