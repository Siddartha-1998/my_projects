#69 and 70 prime and factorial numbers in 1 to 99
for l in range(1,100):
    n = l
    for i in range(2, int(n/2 + 1)):
        if n % i == 0:
            print(" not prime",n)
            break
    else:
            print(" prime",n)
            l+=1
    
    
    