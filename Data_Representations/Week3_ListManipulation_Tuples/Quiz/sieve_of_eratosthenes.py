"""
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    
    answer = list(range(2, bound))
    for divisor in range(2, bound):
        # Remove appropriate multiples of divisor from answer
        for n in range(2, isqrt(bound)):
            if (divisor * n) in answer:
                answer.remove(divisor * n)
    return answer

print(len(compute_primes(200)))
print(len(compute_primes(2000)))
