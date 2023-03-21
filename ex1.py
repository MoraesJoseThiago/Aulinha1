valor = int(input("Fale o numero: "))
num = 1
nume = 1
if valor > 0 and valor < 11:
    for x in range(1, 11):
        num *= valor
        print(f"{valor} x {x}:", num)
        nume += 1
        num = nume
else:
    print("Insira un valor entre 1 e 10")