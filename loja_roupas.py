# Uma loja de roupas precisa de um programa que ajude a calcular o valor final da venda de produtos. Existem algumas regras que precisam ser respeitadas na venda de um produto:
#1 – A vista – 10% de desconto, caso o valor da venda seja maior que 500 15%, caso seja maior que 1000, 20% de desconto;
#2 – A prazo – A venda pode ser parcelada em até 18x. Caso seja parcelado em mais do que 10x possui juros:
#Apenas compras com mais de 800 reais podem ser parceladas acima de 5x;
#Juros:
#1 – 11 vezes: 5% de juros ao mês.
#2 – 12 vezes: 6.5% de juros ao mês.
#3 – 13 vezes: 7% de juros ao mês.
#4 – 14 vezes: 9% de juros ao mês.
#5 – 15 vezes: 9.5% de juros ao mês.
#6 – 16 vezes: 10% de juros ao mês.
#7 – 17 vezes: 11.3% de juros ao mês.
#8 – 18 vezes: 12% de juros ao mês. 
#O usuário informa o valor total da compra, a forma de pagamento e o numero de parcelas. Ao final o programa mostra o valor final.

print ("=====Loja de Roupas=====")
print()

valortotal = float(input("Qual o valor total da compra? R$"))
formapagamento = input("Escolha a forma de pagamento (Vista/Prazo) ")
print ("=============================================================")
print ()

if formapagamento == "Vista":
    if valortotal > 500 and valortotal < 1000:
        desconto = valortotal * 0.1
        print ("Você recebeu um desconto de 10%")
        print (f"O valor final da sua compra é de {valortotal - desconto: .2f}")
    elif valortotal > 1000:
        desconto = valortotal * 0.15
        print ("Você recebeu um desconto de 15%")
        print (f"O valor final da sua compra é de {valortotal - desconto: .2f}")
    elif valortotal < 500:
        print (f"O valor final da sua compra é de {valortotal: .2f}")
elif formapagamento == "Prazo":
    print ("É possível parcelar em até 18x")
    print ("Compras abaixo de 800 só podem ser parceladas até 4x !!!")
    parcelas = int (input ("Gostaria de Parcelar em até quantas vezes? "))
    if parcelas >= 1 and parcelas <= 4 and valortotal <= 800:
        print(f"O valor das parcelas será de {valortotal/parcelas: .2f}")    
    elif parcelas >= 5 and parcelas <= 10 and valortotal > 800:
        print(f"O valor das parcelas será de {valortotal/parcelas: .2f}")
    elif parcelas == 11:
        juros = 0.05
        print("Essa compra possui 5% de juros")
        print(f"Valor final da sua compra é de {(valortotal/parcelas)*juros*11+valortotal: .2f}")
    elif parcelas == 12:
        juros = 0.065
        print("Essa compra possui 6,5% de juros")
        print(f"Valor final da sua compra é de {(valortotal/parcelas)*juros*12+valortotal: .2f}")
    elif parcelas == 13:
        juros = 0.07
        print("Essa compra possui 7% de juros")
        print(f"Valor final da sua compra é de {(valortotal/parcelas)*juros*13+valortotal: .2f}")
    elif parcelas == 14:
        juros = 0.09
        print("Essa compra possui 9% de juros")
        print(f"Valor final da sua compra é de {(valortotal/parcelas)*juros*14+valortotal: .2f}")
    elif parcelas == 15:
        juros = 0.095
        print("Essa compra possui 9,5% de juros")
        print(f"Valor final da sua compra é de {(valortotal/parcelas)*juros*15+valortotal: .2f}")
    elif parcelas == 16:
        juros = 0.1
        print("Essa compra possui 10% de juros")
        print(f"Valor final da sua compra é de {(valortotal/parcelas)*juros*16+valortotal: .2f}")
    elif parcelas == 17:
        juros = 0.113
        print("Essa compra possui 11,3% de juros")
        print(f"Valor final da sua compra é de {(valortotal/parcelas)*juros*17+valortotal: .2f}")
    elif parcelas == 18:
        juros = 0.12
        print("Essa compra possui 12% de juros")
        print(f"Valor final da sua compra é de {(valortotal/parcelas)*juros*18+valortotal: .2f}")
             
