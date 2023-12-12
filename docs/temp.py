list_question_mix = [
    {
        "question": "Python이라는 언어는 어떤 특징을 가지고 있나요?",
        "answer": ["고급 프로그래밍 언어로 간결하고 읽기 쉬운 문법을 가짐", "HTML과 같은 마크업 언어", "하드웨어를 직접 제어할 수 있는 저급 언어", "한 줄씩 소스 코드를 해석해서 실행하지 않는 언어"],
        "correct_index": 0,
        "score": 10
    },
    {
        "question": "Python에서 리스트와 튜플의 차이는 무엇인가요?",
        "answer": ["리스트는 변경 가능하지만 튜플은 변경 불가능함", "리스트는 변경 불가능하고 튜플은 변경 가능함", "리스트와 튜플 모두 변경이 불가능함", "리스트와 튜플 모두 변경이 가능함"],
        "correct_index": 0,
        "score": 10
    },
    {
        "question": "Python에서 'for' 반복문을 어떻게 사용하나요?",
        "answer": ["시퀀스나 다른 반복 가능한 객체의 원소들을 순회", "'for'는 Python에 존재하지 않는 키워드임", "'for' 키워드를 사용하여 조건이 참인 동안 반복", "'for' 키워드를 사용하여 특정 횟수만큼 반복"],
        "correct_index": 0,
        "score": 10
    },
    {
        "question": "Python에서 함수를 어떻게 정의하나요?",
        "answer": ["'def' 키워드를 사용하여 정의", "'function' 키워드를 사용하여 정의", "'fun' 키워드를 사용하여 정의", "'define' 키워드를 사용하여 정의"],
        "correct_index": 0,
        "score": 10
    },
    {
        "question": "Python에서 클래스를 어떻게 정의하고 사용하나요?",
        "answer": ["'class' 키워드를 사용하여 정의", "'object' 키워드를 사용하여 정의", "'cls' 키워드를 사용하여 정의", "'new' 키워드를 사용하여 정의"],
        "correct_index": 0,
        "score": 10
    }
]
dict_question =[]

for i in range(len(list_question_mix)):
    for j in list_question_mix[0].keys():
        dict_question.append(list_question_mix[i][j])
    pass
    
print(dict_question)