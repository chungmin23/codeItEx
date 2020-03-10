# -*- coding: utf-8 -*-

class User:
    def say_hello(self):
        print("안녕하세요! 저는 {}입니다".format(self.name))

    def check_name(self, name):
        #파라미터로 받은 name이 유저의 이름과 같으지 불린으로 리턴하는 메소드
        return self.name == name

user1 = User()
user2 = User()


user1.name = "김대위"
user1.email = "captain@codedit.kr"
user1.pw= "12345"

user2.name = "강영훈"
user2.email ="younghoon@codeit.kr"
user2.pw = "98765"

print(user1.check_name("김대위"))
print(user1.check_name("강영훈"))