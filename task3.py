import math

def is_prime(n):
    if n <= 1:
        return "NO"
    
    if n == 2:
        return "YES"
    
    if n % 2 == 0:
        return "NO"
    
    limit = int(math.sqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return "NO"
            
    return "YES"

num = int(input())
print(is_prime(num))