#---------- Employee monthly pay ---------

pay_rate = 21
hours_worked = 40

gross_monthly_pay = pay_rate * hours_worked * 52 / 12

print(gross_monthly_pay)

taxes = gross_monthly_pay * .2

payout = gross_monthly_pay - taxes

print(payout)

print (f"Employee makes ${gross_monthly_pay} gross monthly pay and will recieve monthly pay ${payout} after taxes ${taxes} are taken out.")