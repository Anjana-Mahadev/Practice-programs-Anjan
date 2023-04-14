def middle_element(a):
    if len(a) % 2 == 0:
        mid_1 = len(a)//2
        mid_2 = mid_1-1
        print("middle elements are {} and  {}".format(a[mid_2], a[mid_1]))
    else:
        mid = len(a)//2
        print("middle element is {}".format(a[mid]))


middle_element([1, 2, 3,4])
