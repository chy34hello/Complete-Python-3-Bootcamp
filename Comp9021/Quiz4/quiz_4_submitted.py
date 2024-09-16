from math import sqrt

from sympy import I

primes = list()
trinumbers = list()
maxGapList = list()
initialIndexes = 0, 0, 0


class TrinumberWithFactors:
    def __init__(self, trinumber, factor_1, factor_2, factor_3):
        self.trinumber = trinumber
        self.factor_1 = factor_1
        self.factor_2 = factor_2
        self.factor_3 = factor_3

    @staticmethod
    def gap(self):
        return min(self.factor_2-self.factor_1, self.factor_3-self.factor_2)


def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve


def generatePrimes(sieve):
    for i in range(2, len(sieve), 1):
        if sieve[i]:
            primes.append(i)


def processAllTrinumbers(n):
    largestTrinumber = 0
    MaxGap = 0
    maxP_1, maxP_2, maxP_3 = initialIndexes

    for i in range(0, len(primes), 1):
        # Performance tweak 1
        if primes[i]**3 > n:
            break

        for j in range(i, len(primes), 1):
            # Performance tweak 2
            if primes[i]*primes[j]**2 > n:
                break

            for k in range(j, len(primes), 1):

                trinumber_with_factors = TrinumberWithFactors(
                    primes[i]*primes[j]*primes[k], primes[i], primes[j], primes[k])
                currentGap = trinumber_with_factors.gap(trinumber_with_factors)

                # Performance tweak 3
                if trinumber_with_factors.trinumber > n:
                    break
                else:
                    trinumbers.append(trinumber_with_factors.trinumber)

                # calculate Max Trinumber and mark their index
                if trinumber_with_factors.trinumber > largestTrinumber:
                    largestTrinumber = trinumber_with_factors.trinumber
                    maxP_1, maxP_2, maxP_3 = i, j, k

                # calculate Max gap and save to a list
                if currentGap > MaxGap:
                    MaxGap = currentGap
                    maxGapList.clear()
                    addToMaxGapList(trinumber_with_factors)
                elif currentGap == MaxGap:
                    addToMaxGapList(trinumber_with_factors)

    largest_trinumber_with_factors = TrinumberWithFactors(
        largestTrinumber, primes[maxP_1], primes[maxP_2], primes[maxP_3])
    return largest_trinumber_with_factors, MaxGap


def addToMaxGapList(max):
    maxGapList.append(max)


def printFinalResults(n, max, maxGap):

    print(f'There is 1 trinumber at most equal to {n}.') if len(trinumbers) <= 1 else print(
        f'There are {len(trinumbers)} trinumbers at most equal to {n}.')
    print(
        f'The largest one is {max.trinumber}, equal to {max.factor_1} x {max.factor_2} x {max.factor_3}.\n')
    print(f'The maximum gap in decompositions is {maxGap}.')
    print(f'It is achieved with:')
    [print(f'  {i.trinumber} = {i.factor_1} x {i.factor_2} x {i.factor_3}')
     for i in maxGapList]


def tri_numbers(n):
    generatePrimes(sieve_of_primes_up_to(n))
    (largestTrinumberWithFactor, maxGap) = processAllTrinumbers(n)
    printFinalResults(n, largestTrinumberWithFactor, maxGap)


tri_numbers(23)
