
n = int(input("enter n:"))
rt = int(n ** 0.5)
for i in range(2,rt+1):
    if n % i == 0:
        break
else:
    print("prime")