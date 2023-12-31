# https://school.programmers.co.kr/learn/courses/30/lessons/12909

# 올바른 괄호
# 문제 설명
# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 문자열 s의 길이 : 100,000 이하의 자연수
# 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
# 입출력 예
# s	answer
# "()()"	true
# "(())()"	true
# ")()("	false
# "(()("	false
# 입출력 예 설명
# 입출력 예 #1,2,3,4
# 문제의 예시와 같습니다.
'''
def solution(s):
    answer = True
    set_list=list(s)
    if set_list.count('(') - set_list.count(')')==0:
        if set_list[0] != '(':
            answer = False
        else :
            counter = 0
            for i in range(len(set_list)-1):
                
                if set_list[i] == set_list[i+1]:
                    counter += 1
                else :
                    for j in range(counter-1):
                        if set_list[i+1] == set_list[i+j+2]:
                            pass
                        else:
                            answer = False
    else:
        answer = False

    return answer
'''

def solution(s):
    answer = True
    set_list=list(s)
    stack =[]
    if set_list[0] == ')':
        answer = False
    else:
        for i in range(len(set_list)):
            if set_list[i] == '(':
                stack.append('(')
            else:
                try:
                    stack.pop()
                except:
                    pass
                pass
        if len(stack) != 0:
            answer = False
    return answer
