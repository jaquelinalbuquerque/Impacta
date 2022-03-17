num = int(input())
resultado = num % 2
if resultado == 0:
    impar_anterior = num-1
    par_posterior = num+2
    print (f'{impar_anterior} {par_posterior}')
else:
    impar_anterior = num-2
    par_posterior = num+1
    print (f'{impar_anterior} {par_posterior}')
    