boleto = float(input("Qual o valor do boleto: "))
porcentual = float(input("Qual o valor dos juros cobrados: "))
dias = int(input("Qual o valor de dias de atraso: "))
porcentagem = 100

valor = boleto + (boleto * (porcentual/porcentagem)) * dias

print("O valor a ser pago é de: ", valor)