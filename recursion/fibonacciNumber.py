def fibonacci(n):
    assert n>=0 and int(n)==n, "The number should be positive"
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


i=int(input("enter the number"))
print(fibonacci(i))