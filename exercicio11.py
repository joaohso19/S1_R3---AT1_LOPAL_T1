num = int(input("Digite um número de 1 a 10: "))
while num <1 or num >10:
    num = int(input("Digite novamente: "))

print(f"Tabuada do {num}:")
for t in range(1, 11):
    print(f"{num} x {t} = {num * t}")