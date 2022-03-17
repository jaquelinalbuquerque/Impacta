inicio = int(input())
fim = int(input())

primos=[]
contador = 0

for valorx in range(inicio,fim+1):
    cont=0

    for valory in range(1,valorx+1):
        if valorx%valory==0:
            cont+=1
    if cont<=2 and cont != 1:
        primos.append(valorx)

qtd = len(primos)

while contador < len(primos):
    print(primos[contador])
    contador+=1
print(f'primos: {qtd}')