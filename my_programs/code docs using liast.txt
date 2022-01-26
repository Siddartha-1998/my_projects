num = 100
c = 0
k = []
m = []

for i in range(1,num+1):
    if i % 2 == 0 and i % 3 == 0:
        k.append(i)
        c+=1
m.append(c)

print(k)
print("count of data:",m)
