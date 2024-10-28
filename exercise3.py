def solve(N):
    x = 1 
    i = 2 
    while i * i <= N:
        p = 0 
        while N % i == 0:
            p += 1 
            N //= i
        x *=(i**(p + 1 )- 1) // (i - 1)
        i+= 1
    if N > 1:
        x *= (N** 2 - 1)// (N-1)
    return x 

N = int(input())
sum = solve(N)
print(sum)