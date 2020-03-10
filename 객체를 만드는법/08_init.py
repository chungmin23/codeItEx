# -*- coding: utf-8 -*-


class User:
    # 특수 메소드 :특정상황에서 자동으로 사용되는 메소드
    # 인스턴스가 생성될때 자동 생성됨
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password

# 인스턴스 변수를 한줄에 선언이 가능합니다
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")




print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)
