f = int(input("Fale o numero: "))
r = 1

for x in range(1, f + 1):
    r *= x

print(f"O fatorial de {f} é {r}")