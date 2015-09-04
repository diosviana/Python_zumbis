#Somar dois numeros 

n = 1 
soma = 0 

while n <= 2: 
    number = int (input ("Qual o %d numero ? " % n ))
    n = n + 1
    soma = number + soma 
print (soma)