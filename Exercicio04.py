numero = int(input("Digite um número inteiro: "))

if numero > 1:
    for i in range(2, int(numero**0.5) + 1):  
        if numero % i == 0:
            print(f"O número {numero} NÃO é primo.")
            break
    else:
        print(f"O número {numero} É primo.")
else:
    print(f"O número {numero} NÃO é primo.")