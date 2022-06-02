#How to calculate power of a number using recursion?

def power(n,m):
    assert m>=0 and int(m)==m,"the expo should be positive only"
    if m==0:
        return 1
    elif m==1:
        return n
    else:
        return n*power(n,m-1)

i=int(input("Enter the base "))
j=int(input("Enter the expo "))
print(power(i,j))