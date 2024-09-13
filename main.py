from datetime import datetime

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

extrato = []
saldo = 0
numero_saques = 0
limite = 500 
LIMITE_SAQUES = 3

def depositar(x):
    global saldo, extrato
    
    if x < 0:
        print("Não é possível depositar valor negativo")
    else:
        hora = datetime.now().strftime("%H:%M:%S")

        extrato.append({"horario": hora, "valor": x, "descrição": "Depósito"})

        saldo += x

        print(f"Depósito de R$ {x:.2f} realizado às {hora}")

    return saldo

def cons_extrato(saldo,extrato):

    mostrar_saldo = f"Seu saldo é: R$ {saldo:.2f}\n"
    linhas = [f"{item['horario']}: R$ {item['valor']:.2f} - {item['descrição']}" for item in extrato]
    extrato_formatado = "\n".join(linhas)
    
    print(mostrar_saldo + extrato_formatado)



def realizar_saque(x):
    global saldo, extrato, numero_saques, limite, LIMITE_SAQUES
    
    hora = datetime.now().strftime("%H:%M:%S")

    if numero_saques >= LIMITE_SAQUES:
            print(f"Limite de saques diário atingido ({LIMITE_SAQUES}).")
    else:
        if x <= 0:
            print("O valor do saque deve ser positivo")
        elif saldo < x:
            print(f"Saldo insuficiente. Seu saldo é: R$ {saldo:.2f}")
        elif x > limite:
            print(f"Não é possível realizar o saque. O valor excede o limite de R$ {limite:.2f}.")
        else:
            saldo -= x   
            numero_saques += 1
            extrato.append({"horario": hora, "valor": x, "descrição": "Saque"})
            print(f"Saque de R$ {x:.2f} realizado às {hora}")

    return saldo

while True:
    opcao = input(menu).strip().lower()

    if opcao == "d":
        print("\nVamos para o Depósito\n\n")
        x = float(input("Qual valor deseja depositar: "))
        depositar(x)

    elif opcao == "s":
        print("\nVamos para o Saque\n\n")
        x = float(input("Qual valor deseja sacar: "))
        realizar_saque(x) 

    elif opcao == "e":
        print("\nVamos para o Extrato\n\n")
        cons_extrato(saldo,extrato)

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Opção inválida, por favor escolha uma opção válida.")