get_num = int(input())

set_list=[]
result=1
for i in range(get_num):
    set_list.append(get_num-(i))
    pass

for i in range(len(set_list)):
    result *= set_list[i]
    pass

print(result)