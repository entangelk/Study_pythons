# class 초기화 방법
dict_initial=[]
dict_initial=dict()
list_car_infor = ['Ford', 'Mustang', 1964, 2500]

# key : value
dict_carinfor = {
  "brand": ["Ford","auuuudi"],
  "model": ["Mustang",'sdkfj'],
  "year": [1964,2235],
  'items' : []
}
list_carinfo = [
    {
        "brand": "Hyundai",
        "model": "Sonata",
        "year": 2020,
        "color": "Black",
        "price": 30000
    },
    {
        "brand": "BMW",
        "model": "320i",
        "year": 2019,
        "color": "Blue",
        "price": 35000
    },
    {
        "brand": "Mercedes-Benz",
        "model": "C200",
        "year": 2018,
        "color": "Silver",
        "price": 40000
    },
    {
        "brand": "Audi",
        "model": "A6",
        "year": 2022,
        "color": "Red",
        "price": 45000
    },
]

model = dict_carinfor["model"]
print('dict_carfor 있는 model name : {}'.format(model[1]))

# 새로운 값 정의
dict_carinfor['color'] = ['red','blue','brown']

dict_carinfor_k5 = {
        "brand": "Kia",
        "model": "K5",
        "year": 2021,
        "color": "White",
        "price": 28000
}

list_car_infor.append(dict_carinfor_k5)

print(list_car_infor)

pass



