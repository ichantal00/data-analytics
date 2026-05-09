Marketing = 1
Human_Resources = 5
Accounting = 10
Legal = 12
IT_dept = 18
Customer_Relations = 20

# dept = [Marketing, Human_Resources, Accounting, Legal, IT_dept, Customer_Relations]

x = 1

if x == 1:
    print("Marketing")
    x = x + 4
if x > 3:
    print("Human_Resources")
    x = x + 10
if x < 12 and x > 5:
    print ("OOPS")
elif x > 12 and x < 28:
    print("IT_dept")
    x = x - 5
if x < 20 and x > 10:
    print("OOPS")
elif x == 10:
    print("Accounting")

if x >= 21:
    print ("OOPS")
else:
    print("Customer Relations")



