letter= '''Dear <|NAME|>,

you are selected!

<|DATE|>'''

NAME= input("enter name:")
DATE= input("enter date:")

letter= letter.replace("<|NAME|>", NAME)
letter= letter.replace("<|DATE|>", DATE)

print(letter)