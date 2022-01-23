#Write a program to read a 3-digit number and find whether the middle digit is
#numerically equal to the sum of the other two digits and prints an appropriate
#response
a =int(input("enter a:"))
n = a % 10
a = int(a / 10)
b = a % 10
a = int(a / 10)
if b == (n+a):
    print("middle number of 2 digits is equal to the sum of other numbers",n)
else:
    print("middle number of 2 digits is equal to the sum of other numbers",n)

