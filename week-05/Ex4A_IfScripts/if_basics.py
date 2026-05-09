#This one was my favorite. I really like if statements

x = 100 
y = 20

if x / y == 5:
    print("x divided by y is 5")
    x = 1
if x * y == y:
    print("now x times y is y")
    x = 10
else:
    print(f"Whoops, x equals" + x)

if x < y:
    print("x is less than y")
    x = x*2
else:
    print("Uh Oh, x is not less than y")

if x > y:
    print("how is x greater than y??")
else:
    print("x is NOT greater than y")

print(f"The value of x is {x} and the value of y is {y}")
          