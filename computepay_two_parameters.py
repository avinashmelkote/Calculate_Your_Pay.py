# Calculate_Your_Pay.py
# Calculate what your pre-tax income will be if you are an hourly worker in the United States who is also covered by overtime pay provisions. 
# Includes TWO parameters
def computepay(hours, rate):
  if hours > 40.0:
    pay = 40.0*rate + (hours-40.0)*1.5*rate
  else:
    pay = hours*rate
  return pay

x = computepay(60, 10)
print x
