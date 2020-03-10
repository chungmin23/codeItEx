# -*- coding: utf-8 -*-


class User:
    count = 0


    def __init__(self,name,email,pw):
        self.name = name
        self.email = email
        self.pw = pw
        #인스턴스를 생성할 때마다 카운터를 샘
        User.count += 1
# 
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")

user1.count = 5



#클래스 변수
#User.count = 1
print(User.count)
print(user1.count)
print(user2.count)
print(user3.count)