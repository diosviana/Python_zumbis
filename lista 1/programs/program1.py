#Exercicio 1, lista 1:

#Declarating Variables

a = 0
b = 0
c = 0

#Condicao de existencia de um triangulo: a < b + c ; b < a + c ; c < a + b

#Input of users

a = int (input ("Qual o primeiro lado ? "))
b = int (input ("Qual o segundo lado ? "))
c = int (input ("Qual o terceiro lado ? "))

#Checking condition
if a > b + c or b > a + c or c > a + b:
    print ("Nao e um triangulo")
#conditionais
else:
    if a == b and b == c: 
        print ("EQUILATERO")
    elif a == b or b == c: 
        print ("ISOSCELES")
    else:
        print ("ESCALENO")
#result: Preguiçoco Perfeccionista
