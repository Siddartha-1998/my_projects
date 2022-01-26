#combination of odd and  even numbers. using list

n = 1
num = 100



for i in range(n,num+1):
    k.append(i)
for j in k:
    if j % 2 == 0 and j % 3 == 0:
        print(j)
        c+=1
print("count of even",c)
