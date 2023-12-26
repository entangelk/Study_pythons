'''
숫자 야구

첫번째 줄에 숫자 3개를 입력한다.
두번째 줄에 도전 횟수를 입력한다.
세번째 줄 부터 맞추는 기회가 주어진다.

- 숫자는 맞지만 위치가 틀렸을 때는 볼
- 숫자와 위치가 전부 맞으면 스트라이크
- 숫자와 위치가 전부 틀리면 아웃이 주어진다.
- 만약 모두 틀렸을 경우 '아웃'이 출력된다.

선택사항)
- 3S가 나올 경우 프로그램 종료
- 입력 양식이 틀릴 경우 재입력

예시)
입력
- 076
- 5
-485
-310
-206
-067
-076

출력
- 아웃
- 0S 1B
- 1S 1B
- 1S 2B
- 3S 0B
'''

def num_baseball():

    while True:
        set_num = list(input())
        if len(set_num) != 3:
            print('입력 형식이 잘못되었습니다. 처음 세팅할 서로 다른 숫자 3개를 입력해주세요')
            continue
        else:
            break
        pass

    while True:
        strike_count=0
        ball_count=0
        get_num = list(input())
        if len(get_num) != 3:
            print('입력 형식이 잘못되었습니다. 확인하실 숫자 3개를 입력해주세요')
            continue
        else:
            for i in range(len(get_num)):
                if set_num[i] == get_num[i]:
                    strike_count+=1
                    pass
                else :
                    if set_num[i] in get_num:
                        ball_count+=1
                        pass
                    pass
                pass
            pass
        if strike_count==0 and ball_count==0:
            print('아웃')
            pass
        else:
            print('{}S {}B'.format(strike_count,ball_count))
            pass
        if strike_count==3:
            print('정답입니다. 프로그램을 종료합니다.')
            break
    return

num_baseball()
