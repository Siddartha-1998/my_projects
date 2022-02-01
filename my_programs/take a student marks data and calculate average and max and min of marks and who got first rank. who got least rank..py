l = [
    [[35, 45, 54], 'john', 'CSE'],
    [[43, 32, 45], 'Amanda', 'EEE'],
    [[63, 37, 35], 'naresh', 'MECH']
]

x = l[0][0] + l[1][0] + l[2][0]
x

a = x[0] + x[1] + x[2]
b = x[3] + x[4] + x[5]
c = x[6] + x[7] + x[8]

print("john a:", a)
print("Amanda b:", b)
print("naresh c :", c)
print("total is:", a + b + c)

max = a + b + c
min = a - b - c

print("toatal max  marks:", max)
print("total min marks:", min)

sum = a + b + c / 389
s = a + b + c  # 389

print("average of all marks:", int(sum))

if a >= b:
    print("first rank", l[0] and l[1] and l[2])

print("least rank", l[2] and l[1])





