#A Company insures its drivers in the following cases.
#1. If the driver is married.
##3. if the driver is unmarried, female and above 25 years of age.
#In all other cases, the driver is not insured. If the marital status, sex, age of the
#driver are the inputs, write a program to determine whether the driver is insured
marital_status = str(input("enter marital_status:"))
sex = str(input("enter sex:"))
age = int(input("enter age:"))
if marital_status == "married":
    print("driver is insured")

if marital_status == "unmarried":
    if age >= 30:
        if sex == 'male':
            print("driver is insured")
else:
    if age >= 25:
        if sex == "female":
            print("driver is insured")
        else:
            print("driver is not insured")
if age <= 25:
    print("driver not insured")

