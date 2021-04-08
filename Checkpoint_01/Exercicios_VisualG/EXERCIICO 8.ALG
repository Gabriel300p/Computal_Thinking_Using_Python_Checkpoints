Algoritmo "Exerciico 8"

Var
  numero1, numero2, numero3, resultado1, resultado2 : real

inicio

//Entrada
escreval("Qual o valor do seu salário: ")
leia(numero1)

escreval("Digite o valor das despesas: ")
leia(numero2)

numero3 <- 1000000


//Processamento

resultado1 := numero1-numero2
resultado2 := numero3 / (resultado1 * 12)

//Saida


escreva("Você será milionário em aproximadamente ", resultado2:2:2, " ano(s)")

Fimalgoritmo