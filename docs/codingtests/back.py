x = int(input())
n = int(input())

total_ab=0

for i in range(n):
    a,b = map(int, input().split())
    total_ab += (a*b)
    pass

if total_ab == x :
    print('Yes')
    pass
else :
    print('No')
    pass