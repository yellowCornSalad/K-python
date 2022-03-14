# 클래스 선언
class Car:
    color = ""
    speed = 0

    def upspeed(self, value):
        self.speed += value
        
    def downspeed(self, value):
        self.speed -= value
    
# 메인 코드
myCar1 = Car()
myCar1.color = "빨강"
myCar1.speed = 20

myCar2 = Car()
myCar2.color = "파랑"
myCar2.speed = 30

myCar3 = Car()
myCar3.color = "노랑"
myCar3.speed = 40

myCar1.upspeed(30)
print("자동차 1의 색상은 %s 이며, 현재 속도는 %dkm 입니다." % (myCar1.color, myCar1.speed))

myCar2.upspeed(60)
print("자동차 2의 색상은 %s 이며, 현재 속도는 %dkm 입니다." % (myCar2.color, myCar2.speed))

myCar1.upspeed(90)
print("자동차 3의 색상은 %s 이며, 현재 속도는 %dkm 입니다." % (myCar3.color, myCar3.speed))