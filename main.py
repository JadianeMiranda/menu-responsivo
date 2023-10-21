print("Bem vindo a lanchonete Tudo Gostoso")

# Exibe na tela o cardápio para os clientes
print("--------------------CARDÁPIO ------------------------")

print("|  CÓDIGO   |     DESCRIÇÃO        |     VALOR      |")
print("|   100     | Cachorro-Quente      |  R$ 9,00       |")
print("|   101     | Cachorro-Quente Duplo|  R$ 11,00      |")
print("|   102     |       X-Egg          |  R$ 12,00      |")
print("|   103     |       X-Salada       |  R$ 13,00      |")
print("|   104     |       X-Bacon        |  R$ 14,00      |")
print("|   105     |       X-Tudo         |  R$ 17,00      |")
print("|   200     |   Refrigerante Lata  |  R$ 5,00       |")
print("|   201     |     Chá Gelado       |  R$4,00        |")
print("-----------------------------------------------------")

# recebe o valor da conta do cliente e a escolha de pedir algo a mais.
total_ru = 0  
escolha = "s"

# o loop verifica atraves de if,elif e else se o código digitado pelo cliente é correspondete ao preço no cardápio
while escolha == "s":  # ultilizando while
    codigo = int(
        input("Entre com o código do lanche desejado :")
    )  # pede ao cliente que digite o código do lanche que deseja
    if codigo == 100:
        total_ru += 9.00  # acumulador
        print("você pediu um cachorro-quente no valor de R$ 9,00")
    elif codigo == 101:
        total_ru += 11.00
        print("você pediu um cachorro-quente duplo no valor de R$ 11,00")
        total_ru += 12.00
        print("Você pediu um X-Egg no valor de R$ 12,00")
    elif codigo == 103:
        total_ru += 13.00
        print("Você pediu um X-salada no valor de R$ 13,00")
    elif codigo == 104:
        total_ru += 14.00
        print("Você pediu um X-Bacon no valor de R$ 14,00")
    elif codigo == 105:
        total_ru += 17.00
        print("Você pediu um X-Tudo no valor de R$ 17,00")
    elif codigo == 200:
        total_ru += 5.00
        print("Você pediu um refrigerante lata no valor de R$ 5,00")
    elif codigo == 201:
        total_ru += 4.00
        print("Você pediu um chá gelado no valor de R$ 4,00")
    else:
        print(
            "Opção inválido!"
        )  # caso o código do lanche seja digitado errado,exibe mensagem de erro e volta ao loop
        continue  # usando o 'continue'
    print("O valor da compra esta em : R$ {:.2f}".format(total_ru))
    escolha = input(
        "Deseja fazer mais algum pedido? (s/n) :"
    )  # pergunta ao cliente se deseja pedir algo mais.
    if escolha == "s":  # valida a escolha para encerrar o pedido
        continue
    else:
        print("Opção inválido!")
        print(
            "O total a ser pago é : R$ {:.2f}".format(total_ru)
        )  # calcula o total final a ser pago
        print("obrigada pela preferência!")
    break  # encerra o loop com o uso do break
