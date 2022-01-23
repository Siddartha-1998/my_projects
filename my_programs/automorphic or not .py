num=int(input(":"))
num_digit= len(str(num))
square = num ** 2
l = square%pow(10,num_digit)
if l == num:
    print("automorphic",num)
else:
    print("not automorphic",num)
