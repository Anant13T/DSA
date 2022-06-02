#greatest common divisor
def gcd(a,b):
    assert int(a)==a and int(b)==b,"the a and b are not positive"
    if a<0:
        a=-1*a
    if b<0:
        b=-1*b
    if b==0:
        return a
    else:
        return gcd(b,a%b)

i=int(input("enter the number 1 "))
j=int(input("enter the number 2 "))
print(gcd(i,j))