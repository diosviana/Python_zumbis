#Checking if year bissext 

#Variable
year = int(input ("Qual o ano ? "))

#Conditionals
if year % 4 == 0:
    if year % 100 != 0:
        print ("BISSEXTO")
    else:
        if year % 400 == 0:
            print ("BISSEXTO")
        else: 
            print ("NAO E BISSEXTO")
else:
    print ("NAO E BISSEXTO") 
