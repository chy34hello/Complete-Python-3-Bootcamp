from math import sqrt
from time import time


# O(nLogn)
def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve


def Eulers_sieve_of_primes_up_to(n):
  sieve = list(range(2, n+1))
  k=-1
  i=0

  while k:
    k=0
    while (factor := sieve[i]*sieve[i+k])<n:
      sieve.remove(factor)
      while (factor:= factor *sieve[i]) <=n:
        sieve.remove(factor)
      k+=1
    i+=1
  return sieve

def Eulers_sieve_of_primes_up_to_Using_set(n):
  global sieve 
  k=-1
  i=0

  while k:
    k=0
    sieve_as_set = set(sieve)
    while (factor := sieve[i]*sieve[i+k])<n:
      sieve_as_set.remove(factor)
      k+=1
    sieve = sorted(sieve_as_set)
    i+=1
  return sieve


def EularLinier (upperBound):
  filter = [False for i in range(upperBound+1)]
  primeNumbers =[]

  for num in range(2, upperBound+1):
    if not filter[num]:
      primeNumbers.append(num)
    for prime in primeNumbers:
      if num*prime>upperBound:
        break
      filter[num*prime] =True
      if num%prime==0:
        break
  return filter




#print(Eulers_sieve_of_primes_up_to_Using_set(49))
sieve = list(range(2, 20_000+1))


# start_time = time()
# sieve_of_primes_up_to(20_000_000)
# passed_time = time() - start_time
# print(f"It took {passed_time}")

start_time = time()
EularLinier(30)
passed_time = time() - start_time
print(f"It took {passed_time}")





# start_time = time()
# Eulers_sieve_of_primes_up_to_Using_set(20_000)
# passed_time = time() - start_time
# print(f"It took {passed_time}")


# start_time = time()
# Eulers_sieve_of_primes_up_to(20_000)
# passed_time = time() - start_time
# print(f"It took {passed_time}")





def tri_numbers(n):
    pass