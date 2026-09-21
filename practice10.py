p1 = "make a lote of money"
p2 = "buy this"
p3 = "click this"
p4 = "trading"

message = input("Enter your message: ")

if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("This comment is a scam ! don't click this type of message")

else:
    print("This comment is not a scam")

print("end of the program")
