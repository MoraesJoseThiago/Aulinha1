print("""As opções são:
1. Candidato Jair Rodrigues
2. Candidato Carlos Luz
3. Candidato Neves Rocha
4. Nulo
5. Branco""")

escolha = 0
escolha1 = 0
escolha2 = 0
escolha3 = 0
escolha4 = 0
escolha5 = 0
while escolha != 6:

    escolha = int(input("Escollha: "))

    if escolha == 1:
        escolha1 += 1

    elif escolha == 2:
        escolha2 += 1

    elif escolha == 3:
        escolha3 += 1

    elif escolha == 4:
        escolha4 += 1

    elif escolha == 5:
        escolha5 += 0

print(f"""Informações:
1. O Candidato Jair Rodrigues teve: {escolha1}
2. Candidato Carlos Luz  teve:   {escolha2}
3. Candidato Neves Rocha  teve: {escolha3}
4. Votos nulos teve: {escolha4}
5. Votos brancos: {escolha5}
""")

if escolha1 > escolha2 and escolha1 > escolha3:
    print("Quem ganhou foi o Jair Rodrigues")
elif escolha2 > escolha1 and escolha2 > escolha3:
    print("Quem ganhou foi o Carlos Luz")
elif escolha3 > escolha1 and escolha3 > escolha2:
    print("Quem ganhou foi o Neves Rocha")
else:
    print("Teve empate entre os candidato")