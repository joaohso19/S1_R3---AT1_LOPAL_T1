L = [5, 7, 2, 9, 4, 1, 3]
l1 = sorted(L)
l2 = sorted(L, reverse = True)
tamanho = len(L)
menor = min(L)
maior = max(L)
soma = sum(L)

print(f"Ordem crescente: {l1}")
print(f"Ordem decrescente: {l2}")
print(f"O tamanho da lista é: {tamanho}")
print(f"O menor valor da lista é: {menor}")
print(f"O maior valor da lista é: {maior}")
print(f"A soma da lista é: {soma}")
