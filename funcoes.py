def cadastro_usuario():

    nome = input("digite o seu nome completo: ")
    cpf = input("digite seu CPF: ")
    nascimento = input("digite sua data de nascimento DD/MM/AAAA: ")

    if len(cpf) != 11:
        print("o seu CPF está incorreto")
        return 'CPF-invalido'
    else:
        conta = {
            "nome": nome,
            "cpf": cpf,
            "data_nascimento": nascimento,
            "saldo": 0,
            "historico": []

        }
    return conta

def menu_opcoes():
    print("==== menu de opções ====")
    print("[1] recarregar o bilhete")
    print("[2] passar na catraca")
    print("[3] verificar saldo")
    print("[4] verificar extrato")
    print("[5] sair")



def recarga(conta):
    valor = input("digite o valor que vai recaregar: ")

    if not valor.isdigit():
        print("digite apenas um número inteiros")
        return
    else:
        valor_int = int(valor)
    
    if valor_int <= 0:
        print("valor do deposito tem que ser maior que 0")
        return

    conta["saldo"] += valor_int
    conta["historico"].append(f"deposito R$ {valor_int}")
    print("recarga realizada com sucesso")

def verificar_saldo(conta):
    print(f"saldo atual R$ {conta["saldo"]}")

def catraca(conta):
    valor = 4.40

    valor_int = valor

    if valor_int >= 4.40:
        conta["saldo"] -= valor_int
        print(" a passagem foi feita com sucesso.")
    else: 
        print("o valor é insuficiente")

def mostra_historico(conta):
    if len(conta["historico"]) <= 0:
        print("não ouve nenhuma movimentação")
    else:
        for resgistro in conta["historico"]:
            print(resgistro)
