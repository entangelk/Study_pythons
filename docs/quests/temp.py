list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"
]

list_answer =  ["좋음", "중간", "좋아지길"]


for i in range(len(list_question)):
    print("{}".format(list_question[i]))
    for j in range(len(list_answer)):
        print("{}. {}".format(j+1,list_answer[j]),end=" ")
        pass
    pass

    # for k in range(3):
    #     print('------------------------')
    #     pass