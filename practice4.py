# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈을 유재석과 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

num_list.extend(mix_list)
print(num_list)



# 사전
cabinet = {3:"유재석", 100:"김태호", 90:"김종국"}
print(cabinet[3])
print(cabinet[100])
print(cabinet[90])

print(cabinet.get(3))
print(cabinet.get(5)) # get은 값이 없으면 none으로 뜨는 특징이 있다
print(cabinet.get(7, "사용 가능"))

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet2 = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet2["A-3"])
print(cabinet2["B-100"])

# 새 손님
cabinet2["A-3"] = "김종국" # 유재석에서 김종국으로 값이 업데이트
cabinet2["C-20"] = "조세호" # 새로 추가
print(cabinet2)

# 떠난 손님
del cabinet2["A-3"] # 제거
print(cabinet2)

# Key만 출력
print(cabinet2.keys())

# Values만 출력
print(cabinet2.values())

# Key & Value 쌍으로 출력
print(cabinet2.items())

# 목욕탕 폐점
cabinet2.clear()
print(cabinet2)



# 튜플

menu = ("돈까스", "치즈 까스")
print(menu[0])
print(menu[1])

# menu.add("생선 까스")

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)



# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 구하기 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))


# 합집합 구하기 (java 를 할 수 있거나 python 을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 구하기 (java 를 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java 를 잊었어요
java.remove("김태호")
print(java)



# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))