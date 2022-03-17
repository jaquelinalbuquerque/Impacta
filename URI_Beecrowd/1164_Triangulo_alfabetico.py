n = int(input())
cont = 1
while cont <= n:
    letra = ord ('A')-1
    print (chr(letra + cont)*cont)
    cont += 1