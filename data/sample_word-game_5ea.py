# 1. word.txt 파일로 부터 단어를 읽어들임
# 2. 제시된 단어 5개까지 타이핑함
# 3. 리스트 단어를 썩어서, 랜덤하게 하나의 단어를 뽑아서 제시함.
# 4. 타이핑한 단어와 비교함.
# 5. 맞췄을 때와, 틀렸을 때 소리를 구분함.
# 6. 걸린시간, 맞춘 갯수 출력
# 7. 3개 이상 맞추면 합격, 2개 이하면 불합격

import pyglet
import time
import random

game_cnt = 1  # 게임 횟수 카운트
correct_cnt = 0  # 단어 맞춘 갯수 카운트
start_time = time.time()
words=[]

with open('./data/word.txt', 'r') as file:
  # 방법1
  read_words = file.readlines()
  print(read_words)
  for word in read_words:
    #print(word.strip().rsplit("\n"))
    # words.append(word.strip().rsplit("\n"))
    words.append(word.strip().rstrip("\n"))

  # 방법2
  # for word in file:
  #   words.append(word.strip())
  
print(words)

input("준비? 엔터를 입력하세요.")

while game_cnt <= 5 :
  # 3. 리스트 단어를 썩어서, 랜덤하게 하나의 단어를 뽑기
  random.shuffle(words)  # words 랜덤하게 썩기
  one_word = random.choice(words)   # words 리스트 중에서 하나 뽑기
  
  print("Question #{}\n{}".format(game_cnt , one_word))
  
  # 타이핑한 단어 변수 넣기
  input_word = input()
  
  # 뽑힌 단어와 타이핑한 단어 비교함.
  if one_word == str(input_word).strip():
    # good.wav 소리내기
    sound = pyglet.resource.media('assets/good.wav', streaming=True)
    sound.play()
    time.sleep(1)  #단위 sec
    # 맞힌 갯수 카운
    correct_cnt = correct_cnt + 1
    # pass 출력
    print("맞춰서~")
  else:
    # bad.wav 소리내기
    sound = pyglet.resource.media('assets/bad.wav', streaming=True)
    sound.play()
    time.sleep(1)  #단위 sec
    # wrong 출력
    print("못맞춰서~")
  print()
  game_cnt = game_cnt + 1  # 게임 횟 증가
end_time = time.time()
#걸린시간 계산 : 게임 종료시간 - 게임 시작시간
game_delay_time = format((end_time - start_time), ".2f")   # 게임 걸릴시간
  
# 3개 이상 맞추면 합격, 2개 이하면 불합격
if correct_cnt >= 3:
  print("합격했습니다.")
else:
  print("불합격했습니다.")
  
#걸린시간, 맞춘 갯수 출력
print(f"게임 걸린시간 : {game_delay_time} 초, 맞춘 갯수 : {correct_cnt} 개")
  

