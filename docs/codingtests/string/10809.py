# https://www.acmicpc.net/problem/10809

# 문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
'''
alfacheck=[]
for i in range(26):
    alfacheck.append(-1)
    pass

alfalist=[]
for i in range(97,123):
    alfalist.append(chr(i))
    pass


get_str=input()
set_list=[]

for i in range(len(get_str)):
    set_list.append(ord(get_str[i]))
    pass


for i in range(len(get_str)):
    if get_str[i] in alfalist:
        char_index_in_alfa = alfalist.index(get_str[i])
        alfacheck[char_index_in_alfa] = get_str.index(get_str[i])
        pass
    else:
        pass
    pass

for i in alfacheck:
    print(i, end=" ")
    pass
'''

def alpha_check():
    get_char=input()
    position_list = list('-1' for i in range(26))
    for i in range(len(get_char)):
        position_list[ord(get_char[i])-97] = str(get_char.index(get_char[i]))
        pass
    return position_list

print(" ".join(alpha_check()))