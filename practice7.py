# 표준 입출력

print("Python", "Java", "JavaScript", sep=", ", end=" ")
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", "JavaScript", file=sys.stdout)
print("Python", "Java", "JavaScript", file=sys.stderr) # 에러처리


scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
		#print(subject, score)
		print(subject.ljust(8), str(score).rjust(4), sep=":")


# 은행 대기 순번표
# 001, 002, 003, ...
for num in range(1, 16):
		print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이나 입력하세요")
print(type(answer)) # 사용자 입력은 항상 문자열로 나옴
print(f"입력하신 값은 {answer} 입니다.")


# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(-500)) # 10자리 공간을 확보하고 오른쪽정렬(>)을 하고 출력

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(1000))
print("{0: >+10}".format(-1000))

# 왼쪽 정렬을 하되, 빈칸으로 _로 채움 +,- 부호도 붙이기
print("{0:_<+10}".format(-300))

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(10000000000000))

# 3자리 마다 콤마를 찍어주기 +,- 부호도 붙이기
print("{0:+,}".format(20000000000000))

# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기, 빈자리는 ^ 로 채워주기
print("{0:^<+30,}".format(80000000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수 까지만 표시 (반올림)
print("{0:.2f}".format(5/3))



# 파일 입출력

score_file = open("score.txt", "w", encoding="utf8") # w = 새로 쓰기 전용
print("수학: 96", file=score_file)
print("영어: 50", file=score_file)
score_file.close()

score_file2 = open("score.txt", "a", encoding="utf8") # a = 추가 전용
score_file2.write("과학 : 80")
score_file2.write("\n코딩 : 98")
score_file2.close()

score_file3 = open("score.txt", "r", encoding="utf8") # r = 읽기 전용
print(score_file3.read()) # 한 번에 다 읽기
score_file3.close()

score_file4 = open("score.txt", "r", encoding="utf8") # r = 읽기 전용
print(score_file4.readline(), end="") # 한줄만 읽고 커서는 다음 줄로 이동
print(score_file4.readline(), end="") # 한줄만 읽고 커서는 다음 줄로 이동
print(score_file4.readline(), end="") # 한줄만 읽고 커서는 다음 줄로 이동
print(score_file4.readline(), end="") # 한줄만 읽고 커서는 다음 줄로 이동
score_file4.close()


score_file5 = open("score.txt", "r", encoding="utf8") # r = 읽기 전용
while True:
	line = score_file5.readline()
	if not line:
		break
	print(line, end="")
score_file5.close()

score_file6 = open("score.txt", "r", encoding="utf8") # r = 읽기 전용
lines = score_file6.readlines() # list 형태로 저장
for line in lines:
	print(line, end="")
score_file6.close()


# pickle
import pickle
profile_file = open("profile.pickle", "wb") # pickle을 사용할 때는 쓰기인 wb로
profile = {"이름": "침착맨", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file2 = open("profile.pickle", "rb") # pickle을 가져올 때는 rb로
profile2 = pickle.load(profile_file2) # file에 있는 정보를 profile에 불러오기
print(profile2)
profile_file2.close()


# with
with open("profile.pickle", "rb") as profile_file:
		print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
		study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file2:
		print(study_file2.read())