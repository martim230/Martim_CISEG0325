nota1 = float(input("Digite a nota da primeira prova (0 a 10): "))
nota2 = float(input("Digite a nota da segunda prova (0 a 10): "))
nota3 = float(input("Digite a nota da terceira prova (0 a 10): "))
peso1 = 2
peso2 = 3
peso3 = 5
media_final = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
if media_final >= 6:
    print(f"Média final: {media_final:.2f} - APROVADO")
else:
    print(f"Média final: {media_final:.2f} - REPROVADO")