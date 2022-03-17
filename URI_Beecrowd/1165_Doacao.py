doacao = float(input())
total = 0
while doacao >=0:
    total += doacao
    doacao = float(input())

print (f'VC$ {total:.2f}')
print (f'R$ {total*2.50:.2f}')