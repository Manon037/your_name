""" import random

print(random.randint(1, 10))

my_list = ["apple", "banana", "cherry"]
print(random.choice(my_list))

print(random.random())

print(random.normalvariate(0, 1)) """

# 모듈화
""" import mod.utils as mu

my_list = ["apple", "banana", "cherry"]
print(mu.rd_int(1, 100))
print(mu.rd_list(my_list))
print(mu.rd_rd())
print(mu.rd_nmvar()) """

# datatime 이용 함수

""" from datetime import datetime as dt

# 현재 시간 출력
import mod.utils as mu
dtnow = mu.get_dtnow()
print(dtnow)

ret = mu.cvt_time2str('2023-09-25')
print(ret)

res = mu.cvt_str2time()
print(res) """

""" print(dt.now())

# 특정 시간대의 현재 시간 출력
# from pytz import timezone
#import timezone
# tz = timezone('Aisia/Seoul')
#tz = timezone('UTC')
#print("timezone : ", dt.now(tz))

# 문자열을 날짜로 변환
data_string = '2021-07-08'
data_object = dt.strptime(data_string, '%Y-%m-%d')
print(data_object)

# 날짜를 문자열로 변환
data_object = dt.now()
data_string = data_object.strftime('%Y-%m-%d')
print(data_string) """

# os 모듈 확인

""" import os

# 현재 작업 디렉토리 출력
print(os.getcwd())

# 디렉토리 변경
os.chdir('../')

# 변경된 디렉토리 출력
print(os.getcwd())

# 파일 목록 출력
print(os.listdir())

# 디렉토리 삭제
os.rmdir('new_directory')
print(os.listdir())

# 디렉토리 생성
os.mkdir('new_directory')
print(os.listdir())
 """
 
""" import mod.utils as mu
import os

print(mu.get_curdir())

pname = "python"
mu.os_mkdir(pname)
print(os.listdir())

os.rmdir(pname)
print(os.listdir) """

""" import sys

print(sys.version)
print(sys.argv) """

#====================
# stack
""" list = []

list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)

print(list)

list.pop()

top = list.pop()
print(top)
print(list)
print(len(list)) """

# append, pop 이용한 queue

# 빈 큐 생성
""" queue = []

# 큐에 값 넣기
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

# 큐의 상태 확인
print(queue)

# 큐에서 값 빼기
front = queue.pop(0)
print(front)
print(queue)
print(len(queue)) """
