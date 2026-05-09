# ----------------------------------------------------------------

# Else if is great for shorter scripts it seems like. or greater than or less than
# while match case seems great for games... I like them both so far!


dept = "marketing"


match dept: 
    case 'marketing': 
        print('Hello to you too!') 
    case other: 
        print('No match found')


# --------- Play Time ----------------------
print("Please select from the following: Marketing, " \
"Human Resources, " \
"Accounting, " \
"Legal, " \
"IT, or " \
"Customer Relations")
dept = input("What dept are you in? ")

match dept:
    case "Marketing":
        print("Welcome to Marketing!")
    case "IT":
        print("Welcome to IT!")
    case "Legal":
        print("Thank you for joining Legal!")
    case "Customer Relations":
        print ("Customer Relations does not begin until 6/1.")
    case "Human Resources":
        print ("Please speak to Human Resources. Just kidding. Welcome to your first day!")
    case "Accounting":
        print ("Accounting classes have already started. Please speak to front desk.")
    case _:
        print ("Please enter a valid choice.")

