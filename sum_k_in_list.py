
#Function that prints pair of neighbouring elements of a list whose sum is k.
def myfunc(a, k):
    for i in range(len(a)-1):
        sum = a[i]+a[i+1]
        if sum == k:
            print([a[i], a[i+1]])


myfunc([1, 2, 3, 4, 1], 5)