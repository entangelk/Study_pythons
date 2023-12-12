list_question_mix = [
    {
        "question":'',
        "answer":[] ,
        "correct_index":0,
        "score": 0
    }
]

## 이건 제가 한거 망했습니다. 다시 고치기에는 너무 먼길을 돌아왔어요
class datainput :
    def __init__(self, dataset) -> None:
        self.dataset= dataset
        self.dict_question=[]
        self.input_dic=[]
        self.input_set=[]
        self.outset = {}
        self.keyset=[]
        self.result=[]
        pass
    
    def incording(self):
        for i in range(len(self.dataset)):
            for j in self.dataset[0].keys():
                self.dict_question.append(self.dataset[i][j])
            pass
        return self.dict_question            



    def input(self):
        get_num=input('추가하실 문제의 갯수를 입력하세요 : ')
        while True:
            try :
                int_get_num = int(get_num)
                for i in range(int_get_num):
                    self.dict_question.append(input('추가하실 질문을 입력하세요 : '))
                    for j in range(4):
                        print('추가한 질문의 보기를 입력하세요 (총 4개중 {}번째) : '.format(j+1))
                        self.get_char = input()
                        self.input_dic.append(self.get_char)
                        pass
                    self.dict_question.append(self.input_dic)
                    self.dict_question.append(int(input('추가한 보기에서 정답의 번호를 입력하세요 : '))-1)
                    self.dict_question.append(int(input('추가한 질문의 점수를 입력하세요 : ')))
                self.input_set.append(self.dict_question)
            except:
                print("숫자가 아닌 다른 문자를 입력하셨습니다. 프로그램을 종료합니다.")
                break
            check = input('입력을 완료하셨으면 Y를 눌러주세요 : ')
            if check == 'Y':
                return self.input_set
            else :
                continue


    def outcording(self):
        for i in self.dataset[0].keys():
            self.keyset.append(i)
            pass

        for i in range(1,len(self.input_set)//4):
            for j in range(4):
                self.outset[self.keyset[j]] = self.input_set[4*i+j]


        return self.outset
    
    def print_data(self):
        print(self.outset)
        return


stfun = datainput(list_question_mix)
stfun.incording()
stfun.input()
stfun.outcording()
stfun.print_data()



## 여기는 gpt에게 수정부분해야할 걸 설명하고 수정한 코드. 잘 동작합니다.
'''
class DataInput:
    def __init__(self, dataset) -> None:
        self.dataset = dataset
        self.dict_question = []

    def input_output(self):
        get_num = input('추가하실 문제의 갯수를 입력하세요 : ')
        while True:
            try:
                int_get_num = int(get_num)
                for i in range(int_get_num):
                    question = input('추가하실 질문을 입력하세요 : ')
                    input_dic = []
                    for j in range(4):
                        choice = input(f'추가한 질문의 보기를 입력하세요 (총 4개중 {j+1}번째) : ')
                        input_dic.append(choice)
                    correct_index = int(input('추가한 보기에서 정답의 번호를 입력하세요 : ')) - 1
                    score = int(input('추가한 질문의 점수를 입력하세요 : '))
                    
                    self.dict_question.extend([question, input_dic, correct_index, score])
            except ValueError:
                print("숫자가 아닌 다른 문자를 입력하셨습니다. 프로그램을 종료합니다.")
                break
            check = input('입력을 완료하셨으면 Y를 눌러주세요 : ')
            if check == 'Y':
                break
        
        # 입력 받은 내용을 출력 형태로 변환하여 반환
        result = []
        keyset = list(self.dataset[0].keys())
        for i in range(0, len(self.dict_question), 4):
            temp_dict = {keyset[j]: self.dict_question[i + j] for j in range(4)}
            result.append(temp_dict)
            
        return result

list_question_mix = [
    {
        "question":'',
        "answer":[] ,
        "correct_index":0,
        "score": 0
    }
]

stfun = DataInput(list_question_mix)
result = stfun.input_output()
print(result)

'''