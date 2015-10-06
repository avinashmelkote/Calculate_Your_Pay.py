# Calculate_Your_Pay.py
# Calculate what your pre-tax income will be if you are an hourly worker in the United States who is also covered by overtime pay provisions. 
hours = float(input("How many hours did you work this week?: "))
rate = float(input("What is your hourly wage?: "))
if hours > 40.0:
    pay = 40.0*rate + (hours-40.0)*1.5*rate
else:
    pay = hours*rate
print("This is how much you will get paid, including overtime pay of 1.5*wage for each hour above 40 hours")
print(pay)
