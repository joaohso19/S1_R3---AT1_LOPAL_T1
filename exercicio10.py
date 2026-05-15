senha = int(input("Digite a senha: "))


while senha != 676767:
    print(f"Acesso negado. Tente novamente! {senha}")
    senha = int(input("Digite novamente: "))


print(f"Acesso liberado. {senha}")