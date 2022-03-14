class Car:
    speed = 0
    def upSpeed(self, value):
        self.speed += value
        
        print("현재 속도 (슈퍼클래스): %d" % self.speed)

class Sedan(Car):
    def upSpeed(self, value):
        self.speed += value

        if self.speed > 150:
            self.speed = 150

        print("현재 속도(서브클래스) : %d" % self.speed)

class Sonata(Car):
    def upSpeed(self, value):
        self.speed += value

        if self.speed > 150:
            self.speed = 150

        print("현재 속도(서브클래스) : %d" % self.speed)



# 서브 클래스(Truck)에는 아무런 내용 없이
# 슈퍼 클래스(car)의 메소드를 그대로 상속
class Truck(Car):
    pass

sedan1, truck1, sonata1 = None, None, None

truck1 = Truck()
sedan1 = Sedan()
sonata1 = Sonata()

# Truck 인스턴스의 upSpeed() 호출하면
# 슈퍼 클래스(Car)의 upSpeed() 메소드 호출
print("트럭 --> ", end = " ")
truck1.upSpeed(200)

#Sedan 인스턴스의 upSpeed() 메소드 호출하면
# 재정의된 upSpeed() 메소드 호출
print("승용차 --> ", end = " ")
sedan1.upSpeed(200)

print("소나타 --> ", end = " ")
sonata1.upSpeed(150)