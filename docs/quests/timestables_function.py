
def cal(get_num):
    if get_num == 20 or get_num == 30 or get_num == 35:
        result=[]
        for counting in range(9):
            result.append(get_num*(counting+1))
            pass
        pass
    else :
        print("이 계산기는 20, 30, 35단만 계산이 가능합니다. 다시 입력해 주세요")
        result=[]
        pass
    return result



while True:
    try:
        str_intro ="확인할 단의 숫자를 입력하세요 : "
        print("{}".format(str_intro))
        get_num = input()
        set_num = int(get_num)
        if set_num == 20 or set_num == 35 or set_num == 30:
            for counting in range(9):
                print("{} * {} = {}".format(set_num,counting+1,cal(set_num)[counting]))
                pass
            pass
        else :
            print("20, 30, 35 이외의 숫자를 입력하셨습니다.")
        pass
    except :
        if get_num == 'q':
         print("프로그램을 종료합니다.")
         break
        else :
            print("20, 30, 35이외의 문자를 입력하셨습니다. 종료를 원하시면 q를 입력해주세요")
            pass
        pass
    pass
