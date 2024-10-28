def solve(n) :
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1) :
        if n % i == 0 :
            return False
    return True

prime = []
for i in range(4294967295, 2147483647 - 1, -1) :
    if solve(i) :
        prime.append(i)
    if len(prime) == 5 :
        break
print(*prime)