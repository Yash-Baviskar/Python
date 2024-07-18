n = int(input("Enter Number:  "))

for i in range(2 ,n):
    
    if(n%i)==0:
        print("this is not a prime number")
        break
else:
    print("this is a prime number")
    