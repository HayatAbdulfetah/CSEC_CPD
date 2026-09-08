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
    count = 0

# another simpler solution 
# n = int(input())

# users = {}

# for _ in range(n):
#     s = input()

#     if s not in users:
#         users[s] = 0
#         print("OK")
#     else:
#         users[s] += 1
#         print(s + str(users[s]))


# Codeforrces problem link --> https://codeforces.com/problemset/problem/4/C
