# https://www.acmicpc.net/problem/11720

# 문제
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

# 출력
# 입력으로 주어진 숫자 N개의 합을 출력한다.
'''
get_num=(int(input()))
get_list=(input())

result = 0
for i in range(get_num):
    result += int(get_list[i])
    pass

print(result)
'''

def char_sum():
    get_num=int(input())
    get_char = input()
    set_list = list(int(get_char[i]) for i in range(get_num))
    result=sum(set_list)
    return result

print(char_sum())
    