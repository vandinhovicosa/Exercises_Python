"""
Áreas do triângulo, Circulo, Trepésio, Quadrado e Retângulo
"""
# entradas
A, B, C = map(float, input("Digite A, B e C:\n").split())

# processamento
triangulo = (A * C)/2.0
circulo = 3.14159 * C ** 2
trapezio = ((A + B) * C)/2.0
quadrado = B ** 2
retangulo = A * B

# saida
print("TRIANGULO: ", str("%.3f"%triangulo))
print("CIRCULO: ", str("%.3f"%circulo))
print("TRAPEZIO: ", str("%.3f"%trapezio))
print("QUADRADO: ", str("%.3f"%quadrado))
print("RETANGULO: ", str("%.3f"%retangulo))
