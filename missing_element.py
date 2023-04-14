def find_missing_element(a):
    a.sort()
    b=[]
    for i in range(a[-1]):
        b=b+[i]
    for k in a:
        if k in b:
            b.remove(k)
    print(b)

find_missing_element([1,3,5,6])
