trabalhos = float(input())
prova = float(input())
media = (trabalhos+prova)/2
if media >= 6.00:
    print ('aprovado')
elif media <6.00 and trabalhos >=2.00:
    print ('talvez com a sub')
else: #media <6.00 and prova <2.00:
    print ('reprovado')