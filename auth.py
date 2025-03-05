def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_upto_n(n):
    """Generate and print prime numbers up to n."""
    primes = [num for num in range(2, n + 1) if is_prime(num)]
    return primes

# Example usage
n = int(input("Enter a number: "))
print("Prime numbers up to", n, ":", prime_numbers_upto_n(n))

