n = int(input())
if (n >= 0) or (n <= 10):
    cont = 1
    while cont <= 10:
        print (f'{n} x {cont} = {n*cont}')
        cont = cont + 1