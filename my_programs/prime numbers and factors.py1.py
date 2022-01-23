n = int(input("enter any number to find:"))
for i in range(1, n//2):
    if   n % i == 0:
        print("not prime",n)
        break
    else:
        print("prime number",n)
        break
for j in range(1,n+1):
    if n % j == 0:
        print(j,"factors of prime number")
    
        

90