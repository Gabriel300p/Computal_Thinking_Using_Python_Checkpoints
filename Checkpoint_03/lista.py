lista = [['julian', '0', '5'], ['ana', '10', '4']]
print(lista)

procurar = input("Digite quem você procura: ")

for i in lista:
    local = lista.index(i) # Primeiro elemento
    for b in i:
        if b == procurar:
            local2 = lista[local].index(b) # Segundo elemento que está dentro do primeiro elemento, pouco confuso, mas é isso aí
            print("Quem você procura está na posição: lista[{}][{}]".format(local,local2))
            break

print("Quem você procura:",lista[local][local2])