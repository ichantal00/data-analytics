# Description: This script tests various numeric 
    # conversion techniques

# Author: Sam Q. Newprogrammer

a = " 101.1 "
b = "55"
c = "402 Stevens"
d = "Number 5"

print (a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# --------- Test each as Integer

a = int( 101.1 ) #worked
b = int(55) #worked
#c = int(402 Stevens) #didnt
#d = int(Number 5) #didnt...

print(a, type(a)) #integer
print(b, type(b)) #integer
#print(c, type(c))
#print(d, type(d))

# ------------ Test each as Float

a = float( 101.1 ) #worked
b = float(55) #worked
#c = float(402 Stevens) #didnt
#d = float(Number 5) #didnt

print(a, type(a)) #float
print(b, type(b)) #float
#print(c, type(c))
#print(d, type(d))

# -------------------- Test a

a = (int(float(101.1)))
b = "55"
c = "402 Stevens"
d = " Number 5 "


print(a, type(a)) #int
print(b, type(b)) #string
print(c, type(c)) #still a string
print(d, type(d))#still  a string

#--------------------- slicing strings

a = (str(int(float( 101.1 ))))
d = " Number 5 "

num1 = a.split("1")
num2 = d.split("b")
print(num1)
print(num2)

# --------- strip the leading/trailing spaces

num3 = a.strip(" ")
num4 = d.strip(" ")
print(num3)
print(num4)