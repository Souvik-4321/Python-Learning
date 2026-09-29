f =open("poem.txt")
content =f.read()
if("twinkle" in content ):
        print("The word twinkle is present in the file")
    
else:
        print("The word twinkle is not present in the file")

# with open("file.txt") as f:
#     content =f.read()
#     if("twinkle" in content ):
#         print("The word twinkle is present in the file")
    
#     else:
#         print("The word twinkle is not present in the file")
