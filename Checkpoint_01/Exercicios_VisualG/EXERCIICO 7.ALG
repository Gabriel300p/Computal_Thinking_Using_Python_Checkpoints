Algoritmo "Exerciico 7"

Var
  numero1, numero3, numero2, resultado : real
	numero4 : inteiro

inicio

//Entrada
escreva("Valor do Boleto: ")
leia(numero1)

escreva("Porcentual de Juros: ")
leia(numero2)

escreva("Número de dias em atraso: ")
leia(numero3)

numero4 <- 100


//Processamento

resultado :=  numero1 + (numero1 * (numero2\numero4)) * numero3

//Saida


escreva("Valor a ser pago é de", resultado)

Fimalgoritmo