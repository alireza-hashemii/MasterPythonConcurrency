# Example1
from math import sqrt
from timeit import default_timer as timer

def is_prime(x):
    if x < 2:
        return False

    if x == 2:
        return True
    
    if x % 2 == 0:
        return False
    
    limit = int(sqrt(x)) + 1
    for i in range(3 , limit , 2):
        if x % i == 0:
            return False
    return True


inpt = [i for i in range(10 ** 13 , 10 ** 13 + 500)]
start = timer()
result = []
for i in inpt:
    if is_prime(i):
        result.append(i)
print('Result 1:', result)
print('Took: %.2f seconds.' % (timer() - start))