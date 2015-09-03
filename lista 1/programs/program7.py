#CAR RENTAL 
#PRICES: SEDAN DAY: R$ 70,00 and KM R$ 0.50
#        HATCH DAY: R$ 60,00 and KM R$ 1.10
#        SUV DAY: R$ 90,00 and KM R$ 1.50

#Declarating Variables 

car = ""
days = 0
km = 0
custDays = 0
custKm = 0
custTotal = 0


#Input of users
days = int (input ("How many days were you with the car ? "))
km = int(input ("How many Km you ran ? "))
car = input ("Whats the car ? SEDAN, SUV or HATCH : ").upper()



#If statements
if car == "SEDAN":
    custDays = days * 70
    custKm = km * 0.5
elif car == "SUV":
    custDays = days * 90
    custKm = km * 1.5
elif car == "HATCH":
    custDays = days * 60
    custKm = km * 0.50
else:
    
    print ("INVALID CAR" )

#Calculating total custs
custTotal = custDays + custKm

#Exit for users
print ("Voce alugou um carro da categoria " +car+ " por %d e isso custara R$ %.2f" %(days, custTotal))

