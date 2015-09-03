#Loja de tintas 


#Declarating Variables
latas = 0
price = 80
m = 0
litros = 0

#Input of users
m = int (input ("Quantos m2 deseja pintar ? "))

#Conditionals
litros = m / 3
latas = litros / 18 
if 54 % latas != 0 : 
    latas = int (latas + 1) 
price = latas * price
print ("Voce precisara de %d latas, isso custara R$ %.2f" % (latas, price)
