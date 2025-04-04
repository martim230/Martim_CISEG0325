segundos = int(input("Digite o número de segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

print(f"{horas}h {minutos}m {segundos_restantes}s")
