n = int(input())
sure = 0

for _ in range(n):
    soln = input()
    correct = soln.count("1")
    
    if correct >= 2:
        sure += 1
        
print(sure)
