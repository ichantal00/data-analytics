hour_pay = float(input("Please input hourly pay: "))
hours = float(input("Please input weekly hours: "))
joint = input("Are you filing jointly? yes/no: ").lower () == "yes"

yearly_gross = hour_pay * hours * 52

if yearly_gross < 12000:
    if joint == False:
        taxes = yearly_gross * .05
        yearly_pay = yearly_gross - taxes
        monthly_pay = yearly_pay / 12
    else:
        yearly_pay = yearly_gross
        monthly_pay = yearly_pay / 12
    print(f"Employee will receive yearly pay of ${yearly_pay}. Monthly pay is ${monthly_pay:.2f}")
elif yearly_gross >= 12000 and yearly_gross <= 24999.99:
    if joint == False:
        taxes = yearly_gross * .1
        yearly_pay = yearly_gross - taxes
        monthly_pay = yearly_pay / 12
    else:
        taxes = yearly_gross * .06
        yearly_pay = yearly_gross - taxes
        monthly_pay = yearly_pay / 12
    print(f"Employee will receive yearly pay of ${yearly_pay}. Monthly pay is ${monthly_pay:.2f}")
elif yearly_gross >= 25000 and yearly_gross <= 74999.99:
    if joint == False:
        taxes = yearly_gross * .15
        yearly_pay = yearly_gross - taxes
        monthly_pay = yearly_pay / 12
    else:
        taxes = yearly_gross * .11
        yearly_pay = yearly_gross - taxes
        monthly_pay = yearly_pay / 12
    print(f"Employee will receive yearly pay of ${yearly_pay}. Monthly pay is ${monthly_pay:.2f}")
else:
    taxes = yearly_gross * .2
    yearly_pay = yearly_gross - taxes
    monthly_pay = yearly_pay / 12
    print(f"Employee will receive yearly pay of ${yearly_pay}. Monthly pay is ${monthly_pay:.2f}")

weekly_pay = monthly_pay / 4

print(f"Employee weekly pay is ${weekly_pay}")