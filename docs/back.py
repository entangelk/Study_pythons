a,b = map(int, input().split())
c = int(input())

d = (b+c)//60
print(d)

if (b+c) < 60:
        print(a, b+c)
        pass
elif (b+c)%60 == 0:
    if a == 23:
        print('0 0')
        pass
    else :
        print(a+d,'0')
        pass        
else :
    if a == 23:
        print('0', (b+c)-60)
        pass
    else :
        print(a+1, (b+c)-60)
        pass