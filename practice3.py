#문자열

sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)


#슬라이스

taeyoon = "040116-1234567"
print("성별 : " + taeyoon[7]) # 7번째 자리 수
print("연 : " + taeyoon[0:2]) # 0부터 2직전까지
print("월 : " + taeyoon[2:4]) # 2부터 2직전까지
print("월 : " + taeyoon[4:6]) # 4부터 6직전까지
print("생년월일 : " + taeyoon[0:6]) # 0부터 6직전까지
print("생년월일 : " + taeyoon[:6]) # 처음부터 6직전까지
print("뒤 7자리 : " + taeyoon[7:14]) # 7부터 14직전까지
print("뒤 7자리 : " + taeyoon[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에부터)" + taeyoon[-7:]) # 맨 뒤에서 7번째부터 끝까지


# 문자열처리함수

amazing = "Python is Amazing"
print(amazing.lower())
print(amazing.upper())
print(amazing[0].isupper())
print(len(amazing))
print(amazing.replace("Python", "Java"))

index = amazing.index("n")
print(index)
index = amazing.index("n", index + 1) # 2번째 위치한 n 찾기
print(index)

print(amazing.find("n"))
print(amazing.find("Java")) # 값이 없으면 -1
# print(amazing.index("Java")) 값이 없으면 오류

print(amazing.count("n")) # n이 몇 번 나오는지


# 문자열 포맷

print("a" + "b")
print("a", "b")

print("나는 %d살입니다." % 20) # %d 대신에 정수값 넣는 것
print("나는 %s을 좋아해요." % "파이썬") # %s 대신에 문자으로 넣는 것
print("Apple은 %c로 시작해요" % "A") # %c 대신에 한글자만 받는 것

print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파랑", "빨강"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파랑", "빨강"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 22, color = "주황"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "주황", age = 22))


# v3.6 이상~
age = 24
color = "노랑"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


# 탈출문자

# \n 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")

# \" \" : 문장 내에서 따옴표
print("저는 '나도코딩' 입니다.")
print('저는 "나도코딩" 입니다.')
print("저는 \"나도코딩\" 입니다.")

# \\ : 문장 내에서 \
print("d:\\work\\code\\portfolio\\PythonWorkspace")

# \r : 커서를 맨 앞으로 이동 -> 해당 글자만큼 앞에서 변환
print("BlueApple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Bluee\bApple")

# \t : 탭
print("Red\tApple")