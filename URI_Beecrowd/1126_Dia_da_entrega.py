dia_compra = input()
if dia_compra == 'domingo':
    dia_num = 0
elif dia_compra =='segunda':
    dia_num = 1
elif dia_compra == 'terca':
    dia_num = 2
elif dia_compra == 'quarta':
    dia_num = 3
elif dia_compra == 'quinta':
    dia_num = 4
elif dia_compra == 'sexta':
    dia_num = 5
elif dia_compra == 'sabado':
    dia_num = 6

prazo = int(input())

if prazo == 0:
    print ('chega hoje!')
else:
    entrega = dia_num + prazo
    if entrega == 7 or entrega == 14:
        print ('sera entregue domingo')
    elif entrega == 1 or entrega == 8:
        print ('sera entregue segunda')
    elif entrega == 2 or entrega == 9:
        print ('sera entregue terca')
    elif entrega == 3 or entrega == 10:
        print ('sera entregue quarta')
    elif entrega == 4 or entrega == 11:
        print ('sera entregue quinta')
    elif entrega == 5 or entrega == 12:
        print ('sera entregue sexta')
    elif entrega == 6 or entrega == 13:
        print ('sera entregue sabado') 

