s=[x**2 for x in range(10)]
print(s)
m=[x for x in s if x%2==0]
print(m)
m.reverse()
print(m)
