from funcoes import *


print("=========================")
print("bem vido ao trafegopago")
print("=========================")


conta_usuario = cadastro_usuario()

while True:
    if conta_usuario != "CPF-invalido":
        print("usuario cadastrado com sucesso \n")
    while True:
        menu_opcoes()
   
        opcao_escolhido = input("qual o número você escolhe: ")

        match opcao_escolhido:
            case "1": recarga(conta_usuario)
            case "2": catraca(conta_usuario)
            case "3": verificar_saldo(conta_usuario)
            case "4": mostra_historico(conta_usuario)
            case "5": 
                print("encerrado o sistema")
                break
    break


print(conta_usuario)