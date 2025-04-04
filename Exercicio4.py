saldo = float(input("Digite o saldo inicial do cliente: "))
cheque = float(input("Digite o valor do cheque: "))
if cheque > saldo:
    print("O cheque não poderá ser descontado. Saldo insuficiente.")
else:
    saldo -= cheque  
    print(f"O cheque foi descontado. Saldo atual: {saldo:.2f}")