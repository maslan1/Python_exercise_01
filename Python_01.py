def slicer(*num):
    evens = []
    odds = []
    for i in num :
        if i % 2 ==0:
            evens.append(i)
        else :
            odds.append(i)
    print("even list : ", evens)
    print("odd list : ", odds)
slicer(1,2,3,4,5,6,7,8,9,11,12,13,14,15,3456,2345,7534)

