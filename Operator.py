"""# 집합
my_set = {1, 2, 3, 4, 5}
print(my_set)

setItem = {5, 3, 1}
print(setItem)"""

"""# 집합 활용
my_set = {5, 8, 3, 7, 1, "h"}

# 출력
print(my_set)
print(*my_set)"""

"""# 생성
my_set = set([5, 8, 3, 7, 1, "h"])
print(my_set)

set_tmp = set("hello")

print(set_tmp)"""

"""# 합집합
my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}

print(my_set | set_item)

print(my_set.union(set_item))

# 차집합
print(my_set - set_item)

print(my_set.difference(set_item))

# 교집합
print(my_set & set_item)

print(my_set.intersection(set_item))

# 추가
print(my_set)

my_set.add(9)

print(my_set)"""

"""# 삭제
my_set = {5, 8, 3, 7, 1, "h"}

print(my_set)

#my_set.clear()
 
print(my_set)

my_set.remove(5)

my_set.discard(2)
print(my_set)"""

"""# 공통된 요소 삭제
my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}

print(my_set)

my_set.difference_update(set_item)
print(my_set)"""

"""# 타입 변환
my_int = 10
print(my_int)

my_str = str(my_int)
print(my_str)

# 변환 확인(1)
print(my_int + 10)
my_str = str(my_int)

print(my_str)

print(my_str + str(10))

print(my_str + "hello")"""

"""# 변환 확인(2)
my_str = '10'
print(my_str)

my_int = int(my_str)
print(my_int)

print(my_int + 10)

my_int2 = int("10")
print(my_int2)"""

"""# 연산자
a = 10
b = 3
# c = a + b
# c = a - b
# c = a / b
# c = a * b
# c = a % b
# c = a // b
c = a ** b

print(c)"""

"""a = 0
print(a)

a += 2
print(a)

a -= 1
print(a)

a *= 4
print(a) 

a /= 2
print(a)

a **= 3
print(a)"""

"""a = 10
b = 4

# c = a > b
# c = a < b
# c = a >= b
# c = a <= b
# c = a == b
c = a != b

print(c)"""

"""a = 1
b = 0

print(a and b)
print(a or b)
print(not b)

x = True
y = False

print(x and y)
print(x or y)
print(not x)
print(not y)"""

"""a = 10
b = 3

# c = a & b
# c = a | b
# c = a ^ b
#c = ~ a
c = a << 2
print(c)

c = a >> 2
print(c)"""

my_list = [9, 4, 3, 7, 8, 'hi']

print(2 not in my_list)

my_dic = {"key1" : "v1", "k2" : "v2"}
print("k" in my_dic)

# x = [1, 2, 4]
# y = [1, 2, 4]
# z = x

#print(x is y)

