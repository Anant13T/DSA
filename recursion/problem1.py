#how to find the sum of digits of a positive integer number using recursion?

def sum1(n):
    assert n>=0 and int(n)==n,"the number should be positive"
    if n==0:
        return 0
    else:
        return int(n%10) + sum1(int(n/10))

i=int(input("Enter the number "))
print(sum1(i))