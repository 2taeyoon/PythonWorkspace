print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
print('풍선')
print("나비")
print('ㅋㅋㅋㅋㅋㅋㅋㅋㅋ')
print('ㅋ'*9)


#참/거짓
print(5>10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))
print(not (5<10))


# 애완동물을 소개해 주세요.
animal = "강아지"
name = "연탄이"
age = 4
hobby = "낮잠"
is_adult = age >= 3

'''
이렇게 하면 주석처리 된다.
'''

print("우리집 " + animal + "의 이름은" + name + "이에요")
hobby = "공놀이"
#print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name,"는", str(age),"살이며,", hobby,"을 아주 좋아해요") # 콤마를 하면 띄어쓰기 생성된다.
print(name + "는 어른일까요?" + str(is_adult))

print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 2의3승
print(5%3) # 나머지 2
print(10%3) # 나머지 1
print(5//3) # 몫 1
print(10//3) # 몫 3

print(10 > 3) # True
print(4 >= 7) #False
print(10 < 3) #False
print(5 <= 5) #True

print(3 == 3) #True
print(4 == 2) #False
print(3 + 4 == 7) #True

print(1 != 3) #True
print(not(1 != 3)) #False

# 둘다 성립 시
print((3 > 0) and (3 < 5)) #True
print((3 > 0) & (3 < 5)) #True

# 하나만 성립 시
print((3 > 0) or (3 > 5)) #True
print((3 > 0) | (3 > 5)) #True

print(5 > 4 > 3) #True
print(5 > 4 > 7) #False


#연산자

print(2 + 3 * 4) #14
print((2 + 3) * 4) #20

number = 2 + 3 * 4
print(number) #14

number = number + 2
print(number) #16

number += 2
print(number) #18

number *= 2
print(number) #36

number /= 2
print(number) #18

number -= 2
print(number) #16

number %= 5
print(number) #1