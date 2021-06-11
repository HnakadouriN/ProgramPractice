x, y = map(int, input().split())
ans = 0
if x + y == 0:
    if x == y:
        ans = x
    ans = 0
if x + y == 1:
    if x == y:
        ans = x
    ans = 2
if x + y == 2:
    if x == y:
        ans = x
    ans = 1
if x + y == 3:
    if x == y:
        ans = x
    ans = 0
if x + y == 4:
    if x == y:
        ans = x
    ans = 0
if x == y:
    ans = x
print(ans)