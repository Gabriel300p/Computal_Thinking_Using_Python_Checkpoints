from datetime import date

data_atual = date.today()

nome = input("Qual o nome do recepcionista? ")
print("\n")
print("Olá,", nome, "Tudo bem?")
yoga = int(input("Quantas pessoas frequentaram a atividade Yoga? "))
natacao = int(input("Quantas pessoas frequentaram a atividade Natação? "))
hidroginastica = int(input("Quantas pessoas frequentaram a atividade Hidroginástica? "))
ginastica = int(input("Quantas pessoas frequentaram a atividade Ginástica Artística? "))

total = yoga + natacao + hidroginastica + ginastica
porcentagem_yoga = (yoga/total) * 100
porcentagem_natacao = (natacao/total) * 100
porcentagem_hidroginastica = (hidroginastica/total) * 100
porcentagem_ginastica = (ginastica/total) * 100

print("\n")
print("Prezado(a)", nome)
print("\n")
print("Na data de hoje (%-1s), %-1s pessoas frequentaram o Clube de Campo Viver a vida com alegria." % (data_atual, total))
print("\n")
print("{:.2f}% da atividade YOGA" .format(porcentagem_yoga))
print("{:.2f}% da atividade NATAÇÃO" .format(porcentagem_natacao))
print("{:.2f}% da atividade HIDROGINÁSTICA" .format(porcentagem_hidroginastica))
print("{:.2f}% da atividade GINÁSTICA ARTÍSTICA" .format(porcentagem_ginastica))

