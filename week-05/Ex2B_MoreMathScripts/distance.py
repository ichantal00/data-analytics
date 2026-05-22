txt = "paper#banana#cat#dog"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 3)

print(x)