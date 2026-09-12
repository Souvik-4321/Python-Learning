p = int(input("Enter a number: "))

for i in range(2,p):
    if(p%i ==0):
        print("the number is not prime")
        break

else:
     print("the number is prime")