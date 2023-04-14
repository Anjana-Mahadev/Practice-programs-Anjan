
a = [1, 2, 3, 4, 5]
ans = []
for i in range(len(a)+1):
    for j in range(i):
        ans = ans+[a[j:i]]
print(ans)
