# Large Prime Generation for RSA
import random
 
# Pre generated primes
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]

def nBitRandom(n):
    return(random.randrange(2**(n-1)+1,2**n-1))

def getLowLevelPrime(n):
    while True:
        prime_candidate = nBitRandom(n)

        for divisor in first_primes_list:
            if prime_candidate % divisor == 0 and divisor**2 <= prime_candidate:
                break
            else:
                return prime_candidate


def isMillerRabinPassed(miller_rabin_candidate):
    '''Run 20 iterations of Rabin Miller Primality test'''
   
    maxDivisionsByTwo = 0
    evenComponent = miller_rabin_candidate-1
   
    while evenComponent % 2 == 0:
        evenComponent >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * evenComponent == miller_rabin_candidate-1)
   
    def trialComposite(round_tester):
        if pow(round_tester, evenComponent, 
               miller_rabin_candidate) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * evenComponent, miller_rabin_candidate) == miller_rabin_candidate-1:
                return False
        return True
   
    # Set number of trials here
    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2,
                       miller_rabin_candidate)
        if trialComposite(round_tester):
            return False
    return True

if __name__ == '__main__':
    while True:
        n = 1024
        prime_candidate = getLowLevelPrime(n)
        if not isMillerRabinPassed(prime_candidate):
            continue
        else:
            print(n, "bit prime is: \n", prime_candidate)
            break
