# https://school.programmers.co.kr/learn/courses/30/lessons/87390

# n^2 배열 자르기
# 제출 내역
# 문제 설명
# 정수 n, left, right가 주어집니다. 다음 과정을 거쳐서 1차원 배열을 만들고자 합니다.

# n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
# i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
# 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
# 1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
# 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.
# 정수 n, left, right가 매개변수로 주어집니다. 주어진 과정대로 만들어진 1차원 배열을 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ n ≤ 107
# 0 ≤ left ≤ right < n2
# right - left < 105
# 입출력 예
# n	left	right	result
# 3	2	5	[3,2,2,3]
# 4	7	14	[4,3,3,3,4,4,4,4]

'''
def solution(n, left, right):
    answer = []
    array = [[i+1 for i in range(n)] for j in range(n)]
    for i in range(1,len(array)):
        for j in range(len(array[i])):
            if array[i][j] < i+1:
                array[i][j] = i+1
    
    for i in array:
        for j in i:
            answer.append(j)

    answer = answer[left:right+1]
    
    return answer
'''

# 1234 2234 3334 4444

def solution(n, left, right):
    answer = ''

    counter = n**2
    # index_list = [i+1 for i in range(n)]
    
    a,b = divmod(counter,left)
    
    re_num = n - a

    # index_list[a]

    long = right - left
    
    for i in range(long):
        if long > n:
            for j in b:
                answer += 
        pass

    return

solution(4	,7	,14)