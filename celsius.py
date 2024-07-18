def f_to_c(f):
    return 5*(f-32)/9  #celsius formula= c=5*(f-32)/9


f=int(input("enter temperture in F:"))
c= f_to_c(f)
print(f"{f_to_c(f)} °C ")