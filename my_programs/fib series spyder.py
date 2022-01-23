n = int(input("enter n:"))
a = 0
b = 1
c = 0
if n == 1:
    print("fib series",a)
else:
    print("not series")
while c <= n:
    print(a)
    sum = a + b
    a = b
    b = sum
    c += 1
