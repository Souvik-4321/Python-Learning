math = int(input("enter marks: "))
physics = int(input("enter marks: "))
chem = int(input("enter marks: "))

total_percentage= (100*(math+physics+chem))/300
if(total_percentage>40 and math>=33 and physics>=33 and chem>=33):
    print("you are passed! good job",total_percentage)
else:
    print("you are failed! try again next time",total_percentage)


