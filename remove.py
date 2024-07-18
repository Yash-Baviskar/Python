def rem(l, word):
    n= []
    for item in l:
        l.remove(word)
        return l
    if not(item==word):
        n.append(item.strip(word))
        return n
    
l=["yash", "tanu", "soni","an"]

print(rem(l,"an"))