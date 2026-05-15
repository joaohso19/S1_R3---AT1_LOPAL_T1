numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial = fatorial * i

print(f"Resultado Final: O fatorial de {numero} é {fatorial}")