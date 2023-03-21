soma = 0

while True:
    num = int(input("Digite os numeros: "))
    if num < 0:
        break 
    soma += num 

print("Soma:", soma)