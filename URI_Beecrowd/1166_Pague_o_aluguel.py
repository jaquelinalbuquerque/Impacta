divida = int(input()) #100
valor_mensal = int(input()) #10
cont = 0

while divida>0: #100
    if divida >= valor_mensal: #100
        antes_pg = divida #100
        divida = divida - valor_mensal #90 
        depois = divida #90
    else:
        antes_pg = divida #10
        divida = divida - divida #10 - 10 = 0
        depois = divida # 0

    cont +=1

    print (f'pagamento: {cont}')
    print (f'antes = {antes_pg}')
    print (f'depois = {depois}')
    print ('-'*5)