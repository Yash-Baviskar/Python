m1= int(input("Enter Sub1 Marks: "))
m2= int(input("Enter Sub2 Marks: "))
m3= int(input("Enter Sub3 Marks: "))

total_percentage = (100*(m1+m2+m3))/300

if(total_percentage>=40 or m1==m2==m3==33):
    print("you are pass")
else:
    print("you are fail try next year !!!")
    