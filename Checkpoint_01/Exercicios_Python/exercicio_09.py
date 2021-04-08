candidato1 = int(input("Quantos votos o candidato A recebeu? "))
candidato2 = int(input("Quantos votos o candidato B recebeu? "))
candidato3 = int(input("Quantos votos o candidato C recebeu? "))
branco = int(input("Quantos brancos? "))
nulos = int(input("Quantos nulos? "))

total_votos = candidato1 + candidato2 + candidato3 + branco + nulos
porcentagem1 = (candidato1 / total_votos) * 100
porcentagem2 = (candidato2 / total_votos) * 100
porcentagem3 = (candidato3 / total_votos) * 100
porcentagem4 = (branco / total_votos) * 100
porcentagem5 = (nulos / total_votos) * 100

print("\n")
print("Total de votos foi de ", total_votos)
print("\n")
print("O candidato A recebeu o total de %-1s votos. Com a porcentagem de %.2f do total" % (candidato1,porcentagem1))
print("O candidato B recebeu o total de %-1s votos. Com a porcentagem de %.2f do total" % (candidato2,porcentagem2))
print("O candidato C recebeu o total de %-1s votos. Com a porcentagem de %.2f do total" % (candidato3,porcentagem3))
print("\n")
print("O total de votos em branco foi de %-1s. Com a porcentagem de %.2f do total" % (branco,porcentagem4))
print("O total de votos nulos foi de %-1s. Com a porcentagem de %.2f do total" % (nulos,porcentagem5))
print("\n")


