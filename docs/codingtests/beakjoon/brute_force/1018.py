# https://www.acmicpc.net/problem/1018

# 문제
# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

# 출력
# 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

def solution_input(a,b):
    board_list=[]

    for i in range(a):
        board_list.append(input())

    return board_list

def soultion_slice(board_list):
    slice_total =[]
    for i in range(len(board_list)-7):
        for j in range(len(board_list[i])-7):
            slice_list = []
            for k in range(8):
                slice_list.append(list(board_list[i:i+8][k][j:j+8]))
            pass
            slice_total.append(slice_list)
    return slice_total

def solution_count(slice_total):
    answer_list=[]
    for i in range(len(slice_total)):
        count = 0
        for j in range(len(slice_total[i])):
            try:
                if slice_total[i][j][0] == slice_total[i][j+1][0]:
                    if slice_total[i][j][0] == 'B':
                        try:
                            slice_total[i][j+1][0] = 'W'
                            count +=1
                        except:
                            pass
                    else :
                        try:
                            slice_total[i][j+1][0] = 'B'
                            count +=1
                        except:
                            pass
            except:
                pass
            for k in range(len(slice_total[i][j])-1):
                if slice_total[i][j][k] == 'B':
                    if slice_total[i][j][k] == slice_total[i][j][k+1]:
                        slice_total[i][j][k+1] = 'W'
                        count+=1
                else :
                    if slice_total[i][j][k] == slice_total[i][j][k+1]:
                        slice_total[i][j][k+1] = 'B'
                        count+=1

        answer_list.append(count)
        
    answer_list.sort()
    return answer_list[0]

a,b = map(int, input().split())

board = solution_input(a,b)
slice_board = soultion_slice(board)
answer = solution_count(slice_board)
print(answer)