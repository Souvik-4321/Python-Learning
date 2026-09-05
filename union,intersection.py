s1= {1,4,5,6,7,8}
s2 = {1,8,9,25,30}

print(s1.union(s2)) # Union method
print(s1.intersection(s2)) #Intersection method

print({1,4}.issubset(s1)) #issubset operation
print(s1.issuperset({1,4})) #issuperset operaion
