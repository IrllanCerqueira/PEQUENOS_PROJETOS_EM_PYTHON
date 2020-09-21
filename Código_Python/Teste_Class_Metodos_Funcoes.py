fibonache = 0
x = 1
y = 0

for i in range(100):
    fibonache = x+y
    x = y
    y = fibonache
    print(fibonache)
