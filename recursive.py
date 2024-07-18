def sum(n):
    if(n==1):
     return 1
    return sum(n-1) +n

print(sum(24))  # 1+2+3+4+.......+n