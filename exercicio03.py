nome = input("Digite seu nome: ")
escada_n = "" #Reserva uma caixa vazia, para cada letra que vamos imprimir.

for letra in nome: # Junta a letra atual ao que já temos.
  escada_n = escada_n + letra
  print(escada_n)