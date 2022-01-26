#uising list even and odd and its count.
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = 0

for i in l:
    if i % 2 == 0:
        print(i)
        c+=1
print("count of even numbers:",c)