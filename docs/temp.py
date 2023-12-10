# for i in range(97, 122):
#     print(i)
#     pass

# alfalist=[]
# for i in range(97,122):
#     alfalist.append(chr(i))
#     pass
# print(type(alfalist[0]))
# for i in range(97, 123):
#     alfalist.index(i)

# print(alfalist)



# a=['abcde']
# a.reverse()
# print(a)

A, B = map(int, input().split())

if A < B :
    print('<')
    pass
elif A>B:
    print('>')
    pass
else:
    print('==')