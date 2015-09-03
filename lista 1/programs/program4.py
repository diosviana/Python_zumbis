#Verificar qual o maior de tres numeros 

#Declating Variables
n1 = 0
n2 = 0
n3 = 0

#Input do usuario
n1 = int (input ("Qual o primeiro numero ? "))
n2 = int (input ("Qual o segundo numero ? "))
n3 = int (input ("Qual o terceiro numero ? "))

#conditionals

if n1 > n2 and n1 > n3: 
    print (n1)
elif n2 > n3 and n2 > n1: 
    print (n2)
else: 
    print (n3)