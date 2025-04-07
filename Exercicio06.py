primos = []

numero = 2


while len(primos) < 10:
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            break
    else:
        primos.append(numero)
    numero += 1

print("Os 10 primeiros números primos são:", primos)