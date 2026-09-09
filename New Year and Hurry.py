n, k = map(int, input().split())

time = 240 - k
total = 0
answer = 0

for i in range(1, n + 1):
    total += 5 * i

    if total <= time:
        answer += 1
    else:
        break

print(answer)

# Codeforces problem link --> https://codeforces.com/problemset/problem/750/A
