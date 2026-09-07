t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    odd = 0
    zero = 0
    two = 0

    for x in a:
        if x % 2 == 1:
            odd += 1
        elif x % 4 == 0:
            zero += 1
        else:
            two += 1

    print(max(odd, zero, two))

# prooblem link --> https://codeforces.com/contest/2259/problem/B
