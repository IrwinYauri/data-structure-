def DecimalToBase(num,b):
    n = num
    if num < 0:
        n*=-1
    
    if(b >= 2 and b <=16):
        rpt = ''
        r = 0
        if n >= b:
            while True:
                r = n%b            
                c = n//b
                n = c
                rpt = nomenclatura(r) + rpt

                if c < b:
                    rpt = str(c) + rpt    
                    break
        else:
            rpt = nomenclatura(n)
    else:
        return ' Note: Limit your solution to bases 2-16 for simplicity'

    if num < 0:
        rpt='-'+rpt
    
    return rpt 

def nomenclatura(v):
    if v == 10:
        return 'A'
    elif v == 11:
        return 'B'
    elif v == 12:
        return 'C'
    elif v == 13:
        return 'D'
    elif v == 14:
        return 'E'
    elif v == 15:
        return 'F'
    else:
        return str(v)    

print(DecimalToBase(14,16))
print(DecimalToBase(14,2))

    
        
