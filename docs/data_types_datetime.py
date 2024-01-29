# datetime은 1~100 일시 증가 방식
# 3월 31일 + 5 = 4월 5일
# 229 + 5 = 235

from datetime import datetime

now = datetime.now()
pass

first_date = datetime(2023,12,20)
# datetime.datetime(2023, 12, 20, 0, 0)

second_date = datetime.strptime("2023-12-25", "%Y-%m-%d")
# datetime.datetime(2023, 12, 25, 0, 0)

result_date = second_date - first_date
pass