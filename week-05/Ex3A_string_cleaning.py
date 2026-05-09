name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

# names lowercased

name_1 = name_1.lower()
name_2 = name_2.lower()
name_3 = name_3.lower()
print(name_1 and name_2 and name_3)

# 1st letters capitalized
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

name_1 = name_1.title(0, 6)
name_2 = name_2.title()
name_3 = name_3.title()
print(name_1 and name_2 and name_3)

#replacing dollar signs with spaces

salary_1 = salary_1.replace("$", " ")
salary_2 = salary_2.replace("$", " ")