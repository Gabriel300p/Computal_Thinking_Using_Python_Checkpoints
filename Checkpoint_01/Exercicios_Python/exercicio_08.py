salario = float(input("Informe o salário: "))
despesas = float(input("Qual o valor das despesas: "))

sobra = salario - despesas
objetivo = 1000000 / (sobra * 12)

print("Vai demorar aproximadamente %.0f Ano(s) para virar milionário" % (objetivo))