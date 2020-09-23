def f(n):
    if n<2:
        return n
    return f(n-1)+f(n-2)

for i in range(3):
    print(i, f(i))
    
