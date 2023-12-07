list=[]

get_list=[]
check_list=[]
for i in range(10):
    get_list.append(0)
    pass
copy_list=get_list.copy()
check_list=get_list.copy()

flag = True
for j in range(10):
    for k in range(10):
        for l in range(10):
            if get_list[l] == copy_list[k-j]:
                copy_list[l] = 1
                print(copy_list)
                if l == 9:
                    flag = True
                    break
            if(flag):
                break
        if(flag):
            break
    else :
        pass
    pass
    pass
