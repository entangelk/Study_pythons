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

    while True: # 입력 부분
        set_num = list(input()) #초기 세팅 숫자 문자열로 입력받아 리스트에 저장
        try:    # 초기 세팅 숫자가 숫자인지 판별
            for i in range(len(set_num)):   
                int(set_num[i])
                pass
        except: # 숫자가 아닌 문자일시
            print('입력 형식이 잘못되었습니다. 처음 세팅할 서로 다른 숫자 3개를 입력해주세요')
            continue    # 다시 처음부터
        if len(set(set_num)) != 3:   # 초기 세팅 숫자의 갯수가 겹치지 않는 3개가 아니라면
            print('입력 형식이 잘못되었습니다. 처음 세팅할 서로 다른 숫자 3개를 입력해주세요')
            continue
        else:   # 정상적으로 입력되었을 시
            break   # 입력 반복문 종료

    while True:
        strike_count=0  # 스트라이크 카운트 초기화
        ball_count=0    # 볼 카운트 초기화
        get_num = list(input()) # 정답 맞춰볼 숫자 문자열로 입력받아 리스트에 저장
        try: # 확인할 숫자가 숫자인지 판별
            for i in range(len(get_num)):
                int(get_num[i])
                pass
        except: # 숫자가 아닌 문자일시
            print('입력 형식이 잘못되었습니다. 처음 세팅할 서로 다른 숫자 3개를 입력해주세요')
            continue
        if len(set(get_num)) != 3:   # 맞춰볼 숫자가 3개가 아니라면
            print('입력 형식이 잘못되었습니다. 확인하실 서로 다른 숫자 3개를 입력해주세요')
            continue
        else:
            for i in range(len(get_num)):   
                if set_num[i] == get_num[i]: # 각 자리수 비교하여
                    strike_count+=1 # 맞다면 스트라이크 카운트 올리기
                    pass
                else :
                    if set_num[i] in get_num:   # 각 자리수가 같지 않을 때, 이외의 자리에 숫자가 존재한다면
                        ball_count+=1   # 볼카운트 올리기
                        pass
                    pass
            if strike_count==0 and ball_count==0:   # 스트라이크, 볼 카운트가 0이라면
                print('아웃')
                pass
            else:
                print('{}S {}B'.format(strike_count,ball_count))    # 스트라이크, 볼 카운트가 0이 아니라면 결과 출력
                pass
            pass

        if strike_count==3: # 만약 스트라이크 카운트가 3일 때
            print('정답입니다. 프로그램을 종료합니다.')
            break   # 반목문 종료
    return

num_baseball()
