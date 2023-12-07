list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"]

list_answer =  ["좋음", "중간", "좋아지길"]

str_que = '당신 생각은 몇 번 : '

set_list_final = []

for num_count_list in range(len(list_question)):    # 리스스 아이템 각각 0으로 초기화
        set_list_final.append(0)

for count in [0, 1, 2, 3]:
    # 질문 명령
        print("{}. {}".format(count+1, list_question[count]))
    # 답안 명령    
        for count_a in [0, 1, 2]:
                   print("{}. {}".format(count_a+1, list_answer[count_a]), end=" ")
                   
    # count가 3보다 작을 때 "----" 출력
        if count < 3 :
    # 다른 행에 나올 수 있도록 분리
                print("")
                print("")
                print("{}".format(str_que), end=" ")    # 이용자 입력 숫자 얻기
                num_get = int(input())
                set_list_final[num_get] + 1     # 입력 숫자별 리스트 숫자 카운팅
                print("----")
# 다른 행에 나올 수 있도록 분리
print("")
print("")
print("{}".format(str_que), end=" ")    #반복 숫자 얻기
num_get = int(input())
set_list_final[num_get] + 1

print("End program!")
    
