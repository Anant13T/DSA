# how to convert a number from decimal to binary using recursion
def conversion1(n):
    assert int(n)==n,"the number should be interger"
    if n == 0:
        return 0
    else:
        return n%2 + 10 * conversion1(int(n/2))
# we can also use the inbuilt function 
# return bin(n).replace("0b","")

i=int(input("enter the number "))
print(conversion1(i))