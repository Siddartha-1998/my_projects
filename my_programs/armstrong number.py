#find given number is arm armstrong or not
n=int(input("enter n:"))
sum = 0
temp = n
digit = n % 10
sum = sum + (digit**3)
i = n//10
if temp == sum :
    print("armstrong",sum)
else:
    print("armstrong not",sum)

