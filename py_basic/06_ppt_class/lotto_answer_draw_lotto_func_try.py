#1 두 수를 입력 받기
#2 랜덤하게 숫자 1개 뽑기(getNumber())
#3 입력 받은 두 수 범위에서 Lotto 숫자 6개 뽑기, 중복되지안게(getLotto())
#4 로또 숫자 터미널에 출력하기(printLotto())
import random

## 함수 정의부
def intputRange():
  try:
    input_value = input("로또를 위한 두 숫자 범위 입력받기 예) 1, 100 >> ")
    num1, num2 = input_value.strip().split(",")
  except ValueError as exception: #Exception
    print(f"{exception}에러입니다.\n숫자를 두개 입력해야합니다.")
    exit()
  else:
    return int(num1), int(num2)  

# 랜덤하게 숫자 1개 뽑기
def getNumber(n1, n2):
  return random.randrange(n1, n2)

# 로또 숫자 뽑기
def getLotto(n1, n2):
  lotto_list =[] # 뽑은 로또 숫자 리스트
  while True:
    num = getNumber(n1, n2)  # 랜덤하게 숫자 뽑기
    
    if num not in lotto_list :
      lotto_list.append(num)
    # lotto_list 갯수가 6이면
    if len(lotto_list) == 6:
      break
  lotto_list.sort()
  #print(lotto_list)
  return lotto_list

def printLotto(lotto) :  
  print()
  print("추첨된 로또 번호 ===>  ", end="")

  # for i in range(0, 6):
  #   print("%d " % lotto_list[i])
  for i in lotto:
    print("%d " % i, end="")
  print()
  

## 메인 코드 부분 ##
print("** 로또 추첨을 시작합니다. ** \n");

# 로또 숫자 범위 입력받기
n1, n2 = intputRange()

# 로또 숫자 6개 뽑기
lotto = getLotto(n1, n2)

# 로또 숫자 출력
printLotto(lotto)

