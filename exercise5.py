def solve(n):
    cnt = 0
    for i in range(1, n+1) :
        if n % i == 0:
            cnt += 1
    if cnt > 2 :
        print(n, ' is a composite number.')
    elif cnt == 2 :
        print(n, ' is prime number.')
    else :
        print(n, ' is a composite number.')
    return cnt
N = int(input())
solve(N)
