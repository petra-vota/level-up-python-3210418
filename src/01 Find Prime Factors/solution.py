# Python Code Challenge #1: Find Prime Factors
# Your goal is to implement a function, `get_prime_factors()`, 
# that takes an integer value as the input argument and 
# returns a list containing all of its prime factors.

#>>> get_prime_factors(630)
#[2, 3, 3, 5, 7]

def get_prime_factors(n):
  prime_factors = []
  i = 2
  while i <= n:
    if not n % i:
      prime_factors.append(i)
      n = n / i
    else:
      i = i+1
  return prime_factors

result = get_prime_factors(630)
print(result)

result = get_prime_factors(13)
print(result)

result = get_prime_factors(60)
print(result)