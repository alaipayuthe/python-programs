"""
Given the pre-defined variables present_value, annual_rate and years, write an assignment statement that define a variable future_value whose value is present_value dollars invested at annual_rate percent interest, compounded annually for years.
"""

# calculate future value

present_value = 50
annual_rate   = 5
years         = 10

future_value  = (present_value * ((1 + (annual_rate * 0.1)) ** years)) 

print("Future value of dollar = " + str(future_value))
