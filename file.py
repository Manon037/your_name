# 파일 생성
# 쓰기 권한, 파일이 없으면 신규 생성
""" file = open("temp.txt", "w")
file.close() """

# 읽기 권한
""" file = open("temp.txt", "r")
file.close() """

# 추가 모드
""" file = open("temp.txt", "a")
file.close() """

# 읽기 및 쓰기 모드
""" file = open("temp.txt", "r+")
file.close() """

# 파일 쓰기
""" file = open("temp.txt", "w")

file.write("hello")
file.write("world")

file.close() """

#\n
""" file = open("temp.txt", "w")

file.write("hello\n")
file.write("world")

file.close() """

# 1 ~ 100
""" file = open("temp.txt", "w")
for i in range(1, 101):
    file.write(f"{i}\n")

file.close() """

#경로
""" file = open("Users\\hwangjeong-a\\Documents\\temp.txt", "w")
for i in range(1, 101):
    file.write(f"{i}\n")

file.close() """