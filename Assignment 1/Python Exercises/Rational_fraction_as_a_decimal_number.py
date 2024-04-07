def fraction_to_decimal(m, n):
    if n == 0:
        return "Error"
    if m == 0:
        return "0"
    if m<0 and n<0:
        negative = False
    elif m<0:
        negative = True
    elif n<0:
        negative = True
    else:
        negative = False
    m, n = abs(m), abs(n)

    list = long_divison(m,n)
    if len(list)==1:
        return '-' + str(m/n) if negative else str(m/n)
    string = str(m//n) + '.'

    for x in list[0]:
        string+= str(x)
    string+='('
    for x in list[1]:
        string+=str(x)
    if negative:
        return '-' + string + ')'
    return string + ')'
def long_divison(m,n):
    seen = {}
    m%=n
    list = []
    cnt = 0
    while m!=0:
        k = (m*10)//n
        list.append(k)
        m = (m*10)%n
        tuple = (k,m)
        if tuple in seen:
            return [list[:seen[tuple]],list[seen[tuple]:-1]]
        seen[tuple] = cnt
        cnt+=1
    return [list]


print(fraction_to_decimal(5,8))
print(fraction_to_decimal(25,9))
print(fraction_to_decimal(19,12))
print(fraction_to_decimal(400,99))
print(fraction_to_decimal(1,28))
print(fraction_to_decimal(7,-12))
print(fraction_to_decimal(-50,8))
print(fraction_to_decimal(0,8))
print(fraction_to_decimal(8,0))

