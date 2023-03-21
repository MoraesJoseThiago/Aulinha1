import random
resultado = random.randint(0, 1)

cara = 0
coroa = 0

quantidade = int(input("Digite a quantidade de vezes que você quer jogar a moeda: "))

while quantidade > 0:
    if resultado == 0:
        print("Cara")
        cara += 1
        quantidade -= 1
        resultado = random.randint(0, 1)

    else:
        print ("Coroa")
        coroa += 1
        quantidade -= 1
        resultado = random.randint(0, 1)


    
print("Quantidade de cara:", cara)
print("Quantidade de Coroa:", coroa) 