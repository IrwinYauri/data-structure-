def BaseToDec(num,b):
    sum = 0
    arr = list(num)
    j = len(num)
    for i in range(len(num)):
        j-=1
        sum += (b**i)*nomenclatura(arr[j])
                
    return sum

def nomenclatura(v):
    valor = 0
    v=v.lower()
    if v == 'a':
        valor = 10
    elif v == 'b':
        valor = 11
    elif v == 'c':
        valor = 12
    elif v == 'd':
        valor = 13
    elif v == 'e':
        valor = 14
    elif v == 'f':
        valor = 15
    else:
        valor = v

    return int(valor)

print(BaseToDec("1110", 2))
print(BaseToDec("EE", 2))
