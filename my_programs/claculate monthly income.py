#Write a program to calculate the monthly income of a person using the
#following commission schedule
#>= Rs.50,000 Rs.375 + 16% sales.
#>= Rs.50,000 but >=Rs.40,000 Rs. 350+14% sales.
#<= Rs.40,000 but >=Rs.30,000 Rs. 325+12% sales.
#<= Rs.30,000 but >=Rs.20,000 Rs. 300+9% sales.
#<= Rs.20,000 but >=Rs.10,000 Rs. 250+5% sales.
#<= Rs.10,000 Rs. 200+3% sales.
rupees = int(input("enter rs:"))
if rupees >= 50000 or rupees>=40000:
    print(rupees * 0.16 + 375)
elif rupees >= 40000 or rupees>=30000:
    print(rupeess * 0.14 + 350)
elif rupees <= 30000 or rupees >=20000:
    print(rupees * 0.12 + 325)
elif rupees <= 30000 or rupees >= 20000:
    print(rupees * 0.9 + 300)
elif rupees <= 20000 or rupees >= 10000:
    print(5 + rupees * 2.5 )
elif rupees <= 10000:
    print(rupees * 0.3 + 200)
