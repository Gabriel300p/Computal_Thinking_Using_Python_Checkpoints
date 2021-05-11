print("-- Boa tarde! Por favor, entre com os valores: --")

pedidos = int(input("Entre com a quantidade de pedidos feitos: "))

while pedidos <= 0:
    print("\nNúmero de pratos principais inválido. Digite novamente")
    pedidos = int(input("Entre com a quantidade de pedidos feitos: "))

valor_nota = float(input("Entre com o valor total da nota: "))

while valor_nota <= 0:
    print("\nValor inválido. Digite novamente")
    valor_nota = float(input("Entre com o valor total da nota: "))

visita = input("O cliente já visitou o restaurante? Responda S para sim e N para não (S/N) ")

visita_maiusc = visita.upper()

while visita_maiusc != "S" and visita != "N":
    print("\nInformação Invalida, digite novamente: ")
    visita = input("O cliente já visitou o restaurante? Responda S para sim e N para não (S/N) ")

cupom = input("Tem algum cupom disponível? Responda S para sim e N para não (S/N) ")

cupom_maiusc = cupom.upper()

contador = 0

if pedidos >= 3:
    desconto_pedidos = valor_nota * 0.04
    print("\n Desconto de 4% adicionado!")
    contador += desconto_pedidos

if valor_nota >= 500:
    desconto_valor = valor_nota * 0.06
    print(" Desconto de 6% adicionado!")
    contador += desconto_valor

if visita_maiusc == "S":
    desconto_visita = valor_nota * 0.05
    print(" Desconto de 5% adicionado!")
    contador += desconto_visita

if cupom_maiusc == "S":
    cupom_desc = input("\n Qual o cupom de desconto? (BORALA10/BORALA5) ")

    if cupom_desc == "BORALA10":
        desconto_borala10 = valor_nota * 0.10
        print("\nDesconto de 10% adicionado!")
        contador += desconto_borala10
        
    elif cupom_desc == "BORALA5":
        desconto_borala5 = valor_nota * 0.05
        print("\nDesconto de 5% adicionado!")
        contador += desconto_borala5
    
    else:
    
        while cupom_desc != "BORALA10" and cupom_desc != "BORALA5":
            print("\nCupom inválido!")
            cupom_maiusc = input("Tem algum cupom disponível? Responda S para sim e N para não (S/N) ")

            if cupom == "S":
                cupom_desc = input("\n Qual o cupom de desconto? (BORALA10/BORALA5) ")
                
                if cupom_desc == "BORALA10":
                    desconto_borala10 = valor_nota * 0.10
                    print("\nDesconto de 10% adicionado!")
                    contador += desconto_borala10
                
                elif cupom_desc == "BORALA5":
                    desconto_borala5 = valor_nota * 0.05
                    print("\nDesconto de 5% adicionado!")
                    contador += desconto_borala5
                
            if cupom == "N":
                print("\nNão tem um cupom válido") 
                break
            
else:
    print("\nSem descontos a mais para adicionar")

desconto_total = valor_nota - contador

dividir = input("\nDeseja rachar o valor? Responda S para sim e N para não (S/N) ")

dividir_maiusc = dividir.upper()

if dividir_maiusc == "S":
    pessoas = int(input("\n São quantas pessoas no total? "))
    divisao = desconto_total / pessoas

    print("\n -----------------------")
    print("Valor da nota sem descontos:")
    print("--> R${}" .format(valor_nota))
    print("Valor da nota com desconto:")
    print("--> R${}" .format(desconto_total))
    print("\nNúmero de pessoas: ")
    print("--> {}" .format(pessoas))
    print("Total por pessoa: ")
    print("--> R${:.2f}" .format(divisao))
    print("-----------------------")

else:
    print("\n -----------------------")
    print("Valor da nota sem descontos:")
    print("--> R${}" .format(valor_nota))
    print("Valor da nota com desconto:")
    print("--> R${}" .format(desconto_total))
    print("-----------------------")

print("\n Finalizou!")
