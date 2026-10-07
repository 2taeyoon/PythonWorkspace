# if문

weather = input("오늘 날씨는 어때요?")
if weather == "비" or weather == "눈": print("우산을 챙기세요")
elif weather == "미세먼지": print("마스크를 챙기세요")
else: print("준비물이 필요 없습니다")

temp = int(input("기온은 어때요?"))
if 30 <= temp : print("너무 더워요. 나가지 마세요.")
elif 10 <= temp and temp < 30: print("괜찮은 날씨입니다.")
elif 0 <= temp < 10: print("외투를 챙기세요.")
else: print("너무 추워요. 나가지마세요.")



# 반복문 for

# randrange()
for waiting_no in range(1, 6): # 1, 2, 3, 4, 5
	print(f"대기번호 : {waiting_no}")

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
	print(f"{customer}커피가 준비되었습니다.")



# 반복문 while
Thor = "토르"
index = 5
while index >= 1:
	print(f"{Thor}, 커피가 준비 되었습니다. {index} 번 남았어요.")
	index -= 1
	if index == 0:
		print("커피는 폐기처분되었습니다.")


# 무한 루프
# IronMan = "아이언맨"
# index2 = 1
# while True:
# 	print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(IronMan, index2))
# 	index2 += 1


customer = "토르"
person = "unknown"

# 조건이 만족할 때까지 계속 반복
while person != customer :
	print("{0}, 커피가 준비 되었습니다.".format(customer))
	person = input("이름이 어떻게 되세요?")



# 컨티뉴
absent = [2, 5] # 결석
no_book = [7] # 책을 잃어버림
for student in range(1, 11): # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
	if student in absent:
		continue
	elif student in no_book:
		print(f"오늘 수업 여기까지 {no_book}은 교무실로 따라와")
		break
	print(f"{student}, 책을 읽어봐")



# 한 줄 for
# 출석번호가 1 2 3 4, 앞에 100을 붙히기로 함 -> 101, 102, 103, 104 ...
students = [1,2,3,4,5]
print(students)
students = [i + 100 for i in students]
print(students)

# 학생 이름을 길이로 변환
attendee = ["Iron Man", "Thor", "Spider Man"]
attendee = [len(i) for i in attendee]
print(attendee)



# 학생 이름을 대문자로 변환
youtuber = ["Superman", "ChimChakMan", "Iron Man"]
youtuber = [i.upper() for i in youtuber]
print(youtuber)