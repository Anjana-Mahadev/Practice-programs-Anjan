my_string = '{this)is (a[string}'
a = 0
b = 0
c = 0
for i in my_string:
    if i == '(':
        a += 1
    if i == ')':
        a -= 1
    if i == '{':
        b += 1
    if i == '}':
        b -= 1
    if i == '[':
        c += 1
    if i == ']':
        c -= 1
if a == 0 and b == 0 and c == 0:
    print(True)
else:
    print(False)
