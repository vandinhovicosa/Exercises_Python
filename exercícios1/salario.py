#entrada
nome=str(input('Digite seu nome: '))
s=float(input('Digite seu salario: '))
v=float(input('Digite as suas vendas: '))
#processamento
sf = s + v * 0.15
m = str("%.1f"%sf)
#saida
print("Seu salário  = ", sf)