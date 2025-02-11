w=input()
lower=0
upper=0
for i in w:
	if i.islower():
		lower+=1
	else:
		upper+=1
if lower>=upper:
	print(w.lower())
else:
	print(w.upper())
