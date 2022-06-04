a=[1,2,3,4,5,"anant","tayal",1.2]
print(1 in a)
for i in range(len(a)):
    print(a[i])
a.insert(0,11)
print(a)
a.append(45)
print(a)
b=[0,9,8,7]
a.extend(b)
print(a)