notas = []

# Lê as notas de 10 alunos
for i in range(1, 11):  # De 1 a 10
    nota = float(input(f"Digite a nota do aluno {i} (0 a 20): "))
    while nota < 0 or nota > 20:  
        print("Nota inválida! Insira uma nota entre 0 e 20.")
        nota = float(input(f"Digite novamente a nota do aluno {i} (0 a 20): "))
    notas.append(nota) 


if len(notas) > 0:  
    media = sum(notas) / len(notas)
    
    print(f"A média das notas dos alunos é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida. Não é possível calcular a média.")