def list_of_primes(l):
    is_prime = [False, False] + [True for x in range(2, l + 1)] 
    i = 2
    while i * i <= l:
        if is_prime[i]:
            for j in range(i*2, l+1, i):
                is_prime[j] = False
        i+=1
    
    return [x for x in range(l+1) if is_prime[x]]

class Primes:
    all_primes = list_of_primes(16000000)
    @staticmethod
    def stream():
        yield from Primes.all_primes