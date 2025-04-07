notas = []

for i in range(1, 11):  
    nota = float(input(f"Digite a nota do aluno {i} (0 a 20): "))
    while nota < 0 or nota > 20:  
        print("Nota inválida! Insira um valor entre 0 e 20.")
        nota = float(input(f"Digite novamente a nota do aluno {i} (0 a 20): "))
    notas.append(nota)

media = sum(notas) / len(notas)

alunos_acima_media = sum(1 for nota in notas if nota >= media)

print(f"\nA média das notas é: {media:.2f}")
print(f"Quantidade de alunos com nota igual ou acima da média: {alunos_acima_media}")