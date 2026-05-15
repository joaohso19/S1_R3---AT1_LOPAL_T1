num = int(input("Digite um número inteiro: "))

if num > 1:
    divisores = 0

    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1

    if divisores == 2:
        print(f"O número {num} é primo.")
    else:
        print(f"O número {num} não é primo")
   