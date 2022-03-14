def func1():
    global a # 전체 a값들을 통일
    a = 10
    print("func1()에서 a값 %d" %a)

def func2():
    print("func2()에서 a값 %d" %a)

a = 20

func1()
func2()