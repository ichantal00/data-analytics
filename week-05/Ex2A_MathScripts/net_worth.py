debts = 30000
assets = 10000
n_w = 10

print (f"Your total assets are ${assets}")
print(f"Your total debts are ${debts}")
print(f"Your net worth is ${n_w}")


#Birthday area of a rectangle

birthday = int(input("What day is your birthday? "))
month = int(input("What month(number) does your birthday fall in? "))
area = birthday * month

print(area)

SideA = birthday
SideB = month

print(f"Side A is {SideA}")
print(f"Side B is {SideB}")

print(f"The area of the rectangle is {area}")


#Restaurant Tip

print("---------------------------------------------------------------")
print("------------------- Restaurant Bill ---------------------------")
print("                                                               ")
res = int(input("Please enter bill amount $ "))
tax = float(input("Please enter tax amount $ "))

tip = res * .15

print (f"The tip on a $ {tip} restaurant bill is $ {res + tax}")
print (f"Total amount is $ {res + tip + tax}")


