import random
numero_secreto = random.randint(1, 100)
print(numero_secreto)

acerto = int(input("Escreva o numero que você acha que é: "))

while acerto != numero_secreto:
    acerto = int(input("Tente novamente:"))
else:
    print("Resposta certa:", numero_secreto)