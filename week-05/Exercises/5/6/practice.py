String1 = "banana apple orange"
words1 = String1.split()
print(words1)


words1 = String1.split("a")
print(words1)

recipe = "flour salt "
recipe = recipe + "pepper"
recipe = recipe.split()
print(recipe)

recipe = 2

while recipe < 10:
    print (recipe)
    recipe += 1

while recipe < 10:
    recipe += 1
    print (recipe)
    

for i in range(7):
    print (i)

for h in range(4):
    print (h)

    my_set = {3, 1, 2}
    print(my_set)

    my_set = {1, 2, 3, 3, 3, 3}
    print(my_set)

    my_set = {1, 2, 3}
    my_set.add(4)
    print(my_set)

    my_set = {1, 2, 3}
    my_set.remove(2)
    print(my_set)

    my_set = {1, 2, 3}
    my_set.discard(2)
    print(my_set)

    my_set = {1,2,3}
    for item in my_set:
        print(item)

   

    states_set = {"maryland", "mississippi", "hawaii", "florida", "utah"}
    print(states_set)
    states_set.add("georgia")
    print(sorted(states_set))
    

day = int(input("Enter a Number "))

if day == 1:
    print("Day of the week: Monday")

elif day == 2:
    print("Day of the week: Tuesday")
    
elif day == 3:
    print("Day of the week: Wednesday")

elif day == 4:
    print("Day of the week: Thursday")

elif day == 5:
    print("Day of the week: Friday")

elif day == 6:
    print("Day of the week: Saturday")

else:
    print("Day of the week: Sunday")


num1 = int(input("Enter a Number "))

if num1 > 0:
    print("good job!")
else:
    print("you're just negative, aren't you?")