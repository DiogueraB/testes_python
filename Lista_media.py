## Exercício 4
# Solicitar nomes dos alunos
# Solicitar notas de 4 provas
# Imprimir o nome dos alunos e suas médias

print("-------------- Lista de Médias --------------")

alunos = []
notas = []
continua = 'S'

while continua == 'S':
    aluno = input("Informe o nome do aluno: ")

    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))
    nota4 = float(input("Informe a quarta nota: "))

    alunos.append(aluno)
    notas.append((nota1, nota2, nota3, nota4))

    continua = input("Deseja inserir mais algum aluno (S/N)?")

for aluno in alunos:
    print(f"Aluno: {aluno}")

    notas_aluno = notas[alunos.index(aluno)]
    media = sum(notas_aluno) / len(notas_aluno)

    print("Média: ", media)



    