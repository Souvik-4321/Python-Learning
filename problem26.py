# Multipication table using function 
def multab(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

n = int(input("Enter a number: "))
multab(n)