n=int(input("enter the number: "))
for i in range(1, n+1): 
 print(""* n ,end="")
 print("*"*(n-i),end="")
 print("*"* (2*i-2),end="")
 print("\n")