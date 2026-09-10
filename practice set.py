name = input("Enter ypur name : ")
print(f"Good morning, {name}" )

letter = '''dear name 
you are selected! on date'''
print(letter.replace("name","souvik").replace("date","29th novemver"))


# detect for double space
s = "souvik  sadhu"
print(s.find("  "))
print(s.replace("  "," "))
print(s)# strings are immuatable that means which cannot be changed by running functionon them
v = "dear Harry,\n\tThis python course is very nice. \nThank you!"
print(v)