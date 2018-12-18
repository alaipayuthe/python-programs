"""
Program that appends the sum of the last two items in fib to the end of fib, given a list fib = [0, 1]
"""

def calculate_fib(num_iterations):
    fib = [0, 1]
    for index in range(num_iterations):
        fib.append((fib[-1] + fib[-2]))
    return fib[-1]

print(calculate_fib(10))
print(calculate_fib(20))
