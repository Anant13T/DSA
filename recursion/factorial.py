def fact(n):
    assert n>=0 and int(n)==n, "the number must be poaitive"
    if n==1 or n==0:
        return 1
    else:
        factorial=n*fact(n-1)
        return factorial

i=int(input("enter the number"))
print(fact(i))