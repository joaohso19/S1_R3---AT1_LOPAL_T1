nome = input("Digite o seu nome: ")
while len(nome) <= 3:
    nome = input("Excedeu o limite de caracterias, digite novamente: ")

idade = int(input("Digite sua idade: "))
while idade <0 or idade >150:
  idade = int(input("Abaixo ou acima do esperado, digite novamente: "))

salario = float(input("Escreva seu salário: "))
while salario <=0 :
  salario = float(input("Inválido, digite novamente: "))

sexo = input("Escreva seu sexo, 'F' para feminino, 'M' para masculino: ").lower()
while sexo != "f" and sexo != "m":
  sexo = input("Escreva seu sexo novamente: ").lower()

estado = input("Escreva seu estado civil, 'S' de solteiro, 'C' de casado, 'V' de viúvo, 'D' de divorciado:").lower()
while estado != "s" and estado != "c" and estado != "v" and estado != "d":
  estado = input("Escreva seu estado civil novamente, 'S' de solteiro, 'C' de casado, 'V' de viúvo, 'D' de divorciado").lower()

print("Cadastro finalizado.:")
print(f"Nome validado: {nome}")
print(f"Idade validada: {idade}")
print(f"salário validado: {salario}")
print(f"Sexo validado: {sexo}")
print(f"Estado civil validado: {estado}")