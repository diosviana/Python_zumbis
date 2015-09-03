#JOAO PAPO DE PESCADOR
#LIMITE: 50 Kg 
#MULTA: R$ 4,00 por Kg 

#Variables

limit = 50
pesqDia = 0
multa = 0
dif = 0

#Input do usuario
pesqDia = int (input ("Joao, quantos quilos de peixe o Sr pescou hoje ? "))
if pesqDia <= limit: 
    print ("NAO PAGARA NENHUMA MULTA")
else:
    dif = pesqDia - limit
    multa = dif * 4
    print ("Pagara, pelo excesso de %d Kg uma multa no valor de R$ %.2f"%(dif, multa))

#Perfeccionismo Preguicoso