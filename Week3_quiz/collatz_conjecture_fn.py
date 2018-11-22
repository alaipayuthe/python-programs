""" This program implements collatz conjecture """

def f(number):
    """
    The function f(n) takes an integer n and divides it by two if n is even and multiplies n by 3 and then adds one to the result if n is odd. 
    """

    if number % 2 == 0:
        return number // 2
    else:
        return (number * 3) + 1

print(f(f(f(f(f(f(f(674))))))))
print(f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071)))))))))))))))
