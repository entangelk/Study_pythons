# https://www.acmicpc.net/problem/2581

# 문제
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

# 입력
# 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

# M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

# 출력
# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 

# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

def solution():
    n=int(input())
    m=int(input())
    get_list=[]
    if n == m:
        count = 0
        for i in range(n):
            if n%(i+1)==0:
                count+=1
                if count == 3:
                    break
        if count ==2:
            print(n)
            print(n)
        else:
            print(-1)
    else:
        for i in range(n,m+1):
            count = 0
            for j in range(i):
                if i%(j+1) == 0:
                    count += 1
                    if count == 3:
                        break
                    pass
            if count == 2:
                get_list.append(i)

        if len(get_list) ==0:
            print(-1)
        else:
            print(sum(get_list))
            print(min(get_list))
    return

solution()