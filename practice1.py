a = int(input("enter your first number: "))
b= int(input("enter yout second number: "))
c= int(input("enter yout third  number: "))
d= int(input("enter yout fourth number: "))

if(a>b and a>c and a>d):
    print("a is greatest number : ",a)
elif(b>a and b>c and b>d):
    print("b is greatest number: ",b)
elif(c>a and c>b and c>d):
    print("c is greatest number: ",c)
else:
    print("d is greatest number: ",d)