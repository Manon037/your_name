"""# 식별 연산 예시
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  
print(x is z)  
print(x is not y)"""

"""# 식별
a = 5
b = 5
print(a is b)
print(a is not b)

print(3 == 3.0)
print(3 is 3.0)"""

"""# 특성
a = [3 , 5, 1]
b = a

print(a is b)
print(a is not b)

a[0] = 2

print(a, b)
print(a is b)
print(a is not b)"""

"""# 연산자 결합 순서
# a = 2 ** 3 ** 2
# a = 2 + 3 * 4 
# a = 10 / 5 / 2
# a = 2 ** 3 ** 2
# a = 2 ** (3 ** 2)
# a = 10 % 3 % 2
# a = 1 + 2 > 3 and 4 - 1 < 2
# a = not False and True
# a = not True or False and True
# a = 1 & 2 | 3 ^ 4
# a = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
# a = 2 * -3 // 2
# a = 1 == 2 != 3

print(a)"""


"""# 조건문 예제
#x = 10
#x = -1
x = 0

if x > 0:
    print("x is positive")

elif x < 0:
    print("x is negative")

else:
    print("x is zero")"""

"""# 조건문 문제

# 1. 짝수, 홀수 구분 조건문 구성  
x = 10
if x % 2 == 0:
    print("x는 짝수이다.")
else:
    print("x는 홀수이다.")

# 2. 두 수를 비교해서 같은지 비교하는 조건문 구성
a = 2
b = 5

if a == b:
    print("값이 같다")
elif a != b:
    print("값이 다르다")"""

"""# 3. 문자가 a or b 인지 비교하는 조건문 구성
x = 'a'

if x == 'a':
    print("a이다.")
elif x == 'b':
    print("b이다.")"""

"""# 반복문
# 반복문 예제
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)"""


"""# 이중 For문 출력
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_list:
    for num in row:
        print(num)"""
        
"""# 1. 0 ~ 9 까지 출력
for i in range(10):
    print(i)"""
        
"""# 2. 문자열을 한글자씩 출력
for char in ("hello"):
    print(char)"""

"""# 3. 리스트 요소 반대로 출력 (reversed 이용)
fruits = ["apple", "banana", "cherry"]

for fruit in reversed(fruits):
    print(fruit)"""

        
"""# 4. 리스트 요소 반대로 출력 (sorted 이용)
fruits = ["apple", "banana", "cherry"]

for fruit in sorted(fruits, reverse=True):
    print(fruit)"""
        
"""# 5. 구구단 출력(이중 for문 이용)
for i in range(1, 10):
    for j in range(1, 10):
        print(i, "x", j, "=", i*j)"""

"""# for ~ else문 예시
rng = [5, 8, 3, 1, 6]

for i in rng:
	print("element : ", i)
else :
	print("end process")"""
 

"""# 반복문 제어 예제
for i in range(10):
    if i == 7:
        print("break", i)
        break
    elif i == 1:
        print("continue", i)
        continue
    else:
        print("pass", i)
        pass

    print(i)"""



"""# While문 예제
i = 1

while i <= 5:
    print(i)
    i += 1"""
    
# While문
# 1. 0부터 9까지 출력
"""i = 0
while i <= 9:
    print(i)
    i += 1"""
    
# 2. 문자열을 한글자씩 출력
"""str_word = "python"
i = 0

while i < len(str_word):
    print(str_word[i])
    i += 1"""
    
# 3. 1부터 10까지의 총합 출력
"""sum = 0
i = 1

while i <= 10:
    sum += i
    i += 1
    
print(sum)"""

"""# 4. 1에서 100까지의 짝수, 홀수 출력하기
#짝수홀수
i = 1
while i <= 100:
    if i % 2 == 0:
        print("짝수 : ", i)
    elif i % 2 == 1:
        print("홀수 : ", i)
    i += 1

# 5. 1에서 100까지의 7의 배수만 출력하기
i = 1

while i <= 100:
    if i % 7 == 0:
        print(i)
    i += 1"""


