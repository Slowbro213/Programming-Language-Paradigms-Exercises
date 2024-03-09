def Representa1ve_value(list):
    avg = sum(list)/len(list)
    representative = 0
    max_diff = abs(avg-list[0])

    for num in list:
        diff = abs(avg-num)
        if(diff<max_diff):
            max_diff=diff
            representative=num
    return representative


list = [9,12.75,14.25,6.3,15.2,8.5,20.5,5.9,7.8,16.4]
print(Representa1ve_value(list))