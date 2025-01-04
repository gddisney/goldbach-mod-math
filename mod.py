from sympy import primerange
from sys import argv
def modular_prime_construction(limit):
    primes = list(primerange(2, limit))  # Generate primes up to the limit
    results = []
    
    for n in range(4, limit, 2):  # Consider even numbers for Goldbach-like exploration
        for x in primes:
            if x >= n:
                break
            for y in primes:
                if y >= n:
                    break
                product = x * y
                z = product % n  # Compute the modular residue
                if product + z == n:  # Verify the decomposition
                    results.append((n, x, y, z))
                    break
    return results

if __name__ == "__main__":
    limit = int(argv[1])  # Adjust to expand the range of n
    results = modular_prime_construction(limit)
    for res in results:
        print(f"{res[0]} = ({res[1]} * {res[2]}) + {res[3]} (z = {res[3]} mod {res[0]})")

