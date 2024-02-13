# https://school.programmers.co.kr/learn/courses/30/lessons/12945

# 피보나치 수
# 제출 내역
# 문제 설명
# 피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

# 예를들어

# F(2) = F(0) + F(1) = 0 + 1 = 1
# F(3) = F(1) + F(2) = 1 + 1 = 2
# F(4) = F(2) + F(3) = 1 + 2 = 3
# F(5) = F(3) + F(4) = 2 + 3 = 5
# 와 같이 이어집니다.

# 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

# 제한 사항
# n은 2 이상 100,000 이하인 자연수입니다.
# 입출력 예
# n	return
# 3	2
# 5	5
# 입출력 예 설명
# 피보나치수는 0번째부터 0, 1, 1, 2, 3, 5, ... 와 같이 이어집니다.

def solution(n):
    answer = 0
    
    if n <= 1:
        return n
    else:
        counter = 0
        result = 0
        iterA = 0
        iterB = 1
        while True:
            counter += 1
            result = iterA + iterB
            iterA = iterB
            iterB = result
            if n-1 == counter:
                break
    answer = result%1234567        
    return answer

solution(5)