# -*- coding: utf-8 -*-

class User:
    # 특수 메소드 :특정상황에서 자동으로 사용되는 메소드
    # 인스턴스가 생성될때 자동 생성됨
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다".format(self.name))

    # 특수 메소드 (dunder 메소드 던더 에스티알 ) - print가 실행이 될때 자동으로 실행이 된다
    def __str__(self):
        return "사용자: {},이메일: {}, 비밀번호: ****".format(self.name,self.email)


user1 = User("강영훈","young@codeit.kr","12345")
user2 = User("이윤수","yooun@codeit.kr","1q2w3e4r5t")

print(user1)
print(user2)