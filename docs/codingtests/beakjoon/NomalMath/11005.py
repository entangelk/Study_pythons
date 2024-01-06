# https://www.acmicpc.net/problem/11005

# 문제
# 10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.

# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

# 입력
# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 10진법 수 N을 B진법으로 출력한다.
seting_data = {
    'A':'10',
    'B':'11',
    'C':'12',
    'D':'13',
    'E':'14',
    'F':'15',
    'G':'16',
    'H':'17',
    'I':'18',
    'J':'19',
    'K':'20',
    'L':'21',
    'M':'22',
    'N':'23',
    'O':'24',
    'P':'25',
    'Q':'26',
    'R':'27',
    'S':'28',
    'T':'29',
    'U':'30',
    'V':'31',
    'W':'32',
    'X':'33',
    'Y':'34',
    'Z':'35',
}

def solution(data, get_num, get_level):
    dic_set = data
    
    answer=''
    while int(get_num) != 0:
        get_num, left_num = divmod(int(get_num), int(get_level))
        if left_num >= 10:
            for key, value in dic_set.items():
                if str(left_num) == value:
                    left_num = key
                    break
        answer += str(left_num)

    return answer[::-1] if answer != '0' else '0'

a, b = input().split()
print(solution(seting_data, a, b))


'''
def solution(data, get_num, get_level):
    dic_set = {int(v): k for k, v in data.items()}  # Value를 Key로 바꿈

    answer=''
    while int(get_num) != 0:
        get_num, left_num = divmod(int(get_num), int(get_level))
        if left_num >= 10:  # 10 이상일 경우 알파벳으로 변환
            left_num = dic_set[left_num]
        answer += str(left_num)
    return answer[::-1]  # 문자열을 뒤집음

a, b = input().split()
print(solution(seting_data, a, b))

'''

