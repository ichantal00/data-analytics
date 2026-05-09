# ----------- Greetings -----------------------------

current_hour = int(input("Please input hour between 1 - 23: "))

if current_hour < 10:
    print("Good Morning!")
    if current_hour < 4:
        print("What are you doing up so late??")
elif current_hour >= 10 and current_hour < 17:
    print ("Good Day!")
else:
    print ("Good Evening!")
    if current_hour >= 22:
        print("What are you doing up so late??")