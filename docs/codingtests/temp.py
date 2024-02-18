def solution(dots):
    dots.sort()
    flag = False
    for i in range(1,len(dots)):
        temp_list = dots.copy()
        dot = dots[i]
        temp_list.remove(dot)
        temp_list.remove(dots[0])
        
        if (dot[0]-dots[0][0])/(dot[1]-dots[0][1]) == (temp_list[1][0]-temp_list[0][0])/(temp_list[1][1]-temp_list[0][1]):
            return 1
        else:
            flag = True
        
    if flag:
        return 0
    
solution([[1, 4], [9, 2], [3, 8], [11, 6]])