inicial = float(input("Me fale o valor inicial: "))
juros = 0.005
meses = 12

for x in range(13):
    montante = inicial * (1 + juros)**x
    print(f"Mês {x}: R${montante}")