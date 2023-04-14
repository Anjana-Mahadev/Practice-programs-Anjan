a = [1, 2, 3, 4, 5]
ans = []
for i in a:
    for j in range(len(a)):
        ans = ans+[[i, a[j]]]

print(ans)
