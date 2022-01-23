#givrn number automorphic or not
num=int(input("enter given number:"))
num_digit= len(str(num))
square = num ** 2
last_digit = square%pow(10,num_digit)
if last_digit == num:
    print("automorphic",num)
else:
    print("not automorphic",num)
