def solution(sizes):
    row = []
    col = []
    total_list = []
    for i in sizes:
        total_list.append(i[0])
        total_list.append(i[1])
    total_list.sort()
    mid = len(total_list)//2
    col = total_list[:mid]
    row = total_list[mid:]

    answer = col[-1]*row[-1]
    return answer

solution([[60, 50]])