#entrada
id1, qtd1, valor1 =map(float, input('Digite informações para peça 1: id, qtd, valor\n:').split())
id2, qtd2, valor2 =map(float, input('Digite informações para peça 2: id, qtd, valor\n:').split())

#processamento
valor_total = (qtd1* valor1)+(qtd2*valor2)

#saida
print("Valor a pagar = R$ ",str("%.1"%valor_total))