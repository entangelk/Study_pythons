def solution(n):
    answer = 0
    for j in range(n):
        counter = 0
        for i in range(1,j+1):
            if (j)%(i) == 0: 
                counter += 1
        if counter >=3:
            answer +=1
    return answer

solution(10)