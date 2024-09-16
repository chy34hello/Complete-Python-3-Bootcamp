from math import sqrt
from time import time

Primes = list()
Trinumbers = list()
maxGapList =list()



def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve

def generatePrimeList(sieve):
  for i in range(2, len(sieve),1):
    if sieve[i]:
      Primes.append(i)

def generateTrinumber(n):
  largest = 8
  MaxGap = 0
  x,y,z =0,0,0


  # 3 nested for loops with performance tweak
  for i in range(0, int(pow(len(Primes),1/3)),1):
    for j in range(i, len(Primes),1):

      # Performance tweak 1
      if Primes[i]*Primes[j]**2 > n:
        break
      for k in range(j, len(Primes),1):
        Trinumber = Primes[i]*Primes[j]*Primes[k]
        gap = min(Primes[j]-Primes[i], Primes[k]-Primes[j])
       
        # Performance tweak 2
        if Trinumber > n:
          break
       
        #calculate Max Trinumber and mark their index
        if Trinumber > largest:
          largest = Trinumber
          x=i
          y=j
          z=k

        #calculate Max gap and save to a list
        if gap > MaxGap:
          MaxGap =gap
          maxGapList.clear()
          maxGapList.append((Trinumber,Primes[i],Primes[j],Primes[k]))
        elif gap == MaxGap:
          maxGapList.append((Trinumber,Primes[i],Primes[j],Primes[k]))

        Trinumbers.append(Trinumber)

  return largest,Primes[x],Primes[y],Primes[z], MaxGap


def tri_numbers(n):
  generatePrimeList(sieve_of_primes_up_to(n))
  Largest,a,b,c, Gap = generateTrinumber(n)
  if len(Trinumbers)>1:
    print(f'There are {len(Trinumbers)} trinumbers at most equal to {n}.')
  else:
    print(f'There is 1 trinumber at most equal to {n}.')
  print(f'The largest one is {Largest}, equal to {a} x {b} x {c}.')
  print()
  print(f'The maximum gap in decompositions is {Gap}.')
  print (f'It is achieved with:')
  for item in maxGapList:
    print(f'{item[0]} = {item[1]} x {item[2]} x {item[3]}')


