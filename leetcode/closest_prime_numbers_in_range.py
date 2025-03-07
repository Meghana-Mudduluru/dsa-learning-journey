import math


def sieve(limit: int) -> list[bool]:
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime


class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:

        is_prime = sieve(right)
        primes = [num for num in range(left, right + 1) if is_prime[num]]

        if len(primes) < 2:
            return [-1, -1]

        min_diff = float('inf')
        ans = [-1, -1]

        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] < min_diff:
                min_diff = primes[i + 1] - primes[i]
                ans = [primes[i], primes[i + 1]]

        return ans

# Creating an object and testing
if __name__ == "__main__":
    sol=Solution()
    left, right = 4,6 # 10,19
    result = sol.closestPrimes(left, right)
    print("Closest prime pair:", result)
