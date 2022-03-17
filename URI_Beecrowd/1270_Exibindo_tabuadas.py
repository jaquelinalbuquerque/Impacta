A = int(input())
B = int(input())

if A <= B:
    
    for i in range (A,(B+1)):
        n = 1
        while n<=10:
            print(f'{i} x {n} = {i*n}')
            n += 1
        print('----------')
else:
    print('Nenhuma tabuada no intervalo!')