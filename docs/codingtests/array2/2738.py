# https://www.acmicpc.net/problem/2738

# 문제
# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

# 출력
# 첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.
'''
get_row, get_col = map(int, input().split())

arrays = []
for j in range(get_row):
    row = []
    for i in range(get_col):
        row.append(0)
    arrays.append(row)

for k in range(2):
        for j in range(get_col):
            get_list=list(map(int, input().split()))
            for l in range(get_row):
                arrays[j][l] += get_list[l]
            pass
        pass

result=[]

for i in range(len(arrays)):
    for j in arrays[i]:
        print(j, end=" ")
        pass
    print("")
    pass
'''

get_row, get_col = map(int, input().split())

# 배열 A 초기화
arrays_A = []
for j in range(get_row):
    row = list(map(int, input().split()))
    arrays_A.append(row)

# 배열 B 초기화
arrays_B = []
for j in range(get_row):
    row = list(map(int, input().split()))
    arrays_B.append(row)

# 결과 배열 초기화
result_arrays = []
for j in range(get_row):
    row = []
    for i in range(get_col):
        row.append(arrays_A[j][i] + arrays_B[j][i])
    result_arrays.append(row)

# 결과 출력
for row in result_arrays:
    for element in row:
        print(element, end=" ")
    print("")