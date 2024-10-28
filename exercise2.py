
import random
SEED, MIN, MAX, N = 1987, 123, 4567, 89
random.seed(SEED)
S = random.sample(range(MIN, MAX), N)
MinS = min(S)
index_S = S.index(MinS)
print(MinS, index_S)