# 함수
def open_account():
	print("새로운 계좌가 생성되었습니다.")

open_account()

# 전달값과 반환값
def deposit(balance, money): #입금
	print(f"입금이 완료되었습니다. 잔액은 {money}원 입니다.")
	return balance + money

def withdraw(balance, money): #출금
	if balance >= money : 
		print(f"출금이 완료되었습니다. 잔액은 {money}원 입니다.")
		return balance - money
	else :
		print(f"잔액이 부족합니다. 잔액은 {money}원 입니다.")

def withdraw_night(balance, money): #저녁에 출금
		commission = 100 # 수수료 100원
		return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print(f"수수료는 {commission}원이며 잔액은 {balance}원입니다.")



# 기본값
def profile(name, age=17, main_lang="Python"):
	print(f"이름: {name} 나이: {age} 주 사용 언어: {main_lang}")

profile("이병건", 20, "Python")
profile("침착맨", 20, "Java")
profile("침바오")
profile("침돌이")
profile("침순이")



# 키워드
def profile2(name, age, main_lang):
		print(name, age, main_lang)

profile2(name="이병건", main_lang="C#", age=20)
profile2(age=25, name="침바오", main_lang="Java")



# 가변인자
# def profile3(name, age, lang1, lang2, lang3, lang4, lang5):
# 	print(f"이름: {name}, 나이: {age}", end=" ")
# 	print(lang1, lang2, lang3, lang4, lang5)

def profile3(name, age, *language):
	print(f"이름: {name}, 나이: {age}", end=" ")
	for lang in language:
			print(lang, end=" ")
	print()

profile3("침착맨", 22, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile3("침순이", 25, "Kotlin", "Swift")



# 지역변수와 전역변수

k2 = 10

def checkpoint(soldier): # 경계근무
	global k2 # 전역변수
	k2 = k2 - soldier
	print(f"[함수 내] 남은 총: {k2}")

def checkpoint_ret(k2, solidier):
	k2 = k2 - solidier # 지역변수
	print(f"[함수 내] 남은 총: {k2}")
	return k2

print(f"전체 총: {k2}")
# checkpoint(2) # 근무 인원
k2 = checkpoint_ret(k2, 3)
print(f"남은 총: {k2}")