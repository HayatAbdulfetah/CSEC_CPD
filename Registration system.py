n = int(input())
stack = []
count = 0
for _ in range(n):
  s = input()
  
  if s in stack:
    count += 1
    print(s + str(count))
  else:
    stack.append(s)
    print("OK")

# Codeforrces problem link --> https://codeforces.com/problemset/problem/4/C
