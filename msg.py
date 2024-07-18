p1 ="make a lot of money"
p2= " but now"
p3 = "subscribe this"
p4="click this"

msg = input("enter your comment: ")

if((p1 in msg.lower()) or (p2 in msg.lower()) or (p3 in msg.lower()) or (p4 in msg.lower())):
    
     print("this comment is a spam")
     
else:
    print("this comment is not a spam")