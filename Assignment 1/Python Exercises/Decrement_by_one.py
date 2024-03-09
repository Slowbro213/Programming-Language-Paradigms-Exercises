def Decrement_By_One(array):
    n = len(array)
    if(n==0):
        return
    array[-1]-=1
    if(n==1):
        return
    for i in range(n-1):
        if array[-i-1] <0:
            array[-i-1]=9
            array[-i-2]-=1
    if array[0]==0 :
        array.pop(0)



list = [2,3,4]
Decrement_By_One(list)
print(list)
list = [3,1]
Decrement_By_One(list)
print(list)
list = [1,0,0]
Decrement_By_One(list)
print(list)
list = [1]
Decrement_By_One(list)
print(list)
list = [0]
Decrement_By_One(list)
print(list)