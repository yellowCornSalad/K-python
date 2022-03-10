# https://pyglet.readthedocs.io/en/latest/programming_guide/quickstart.html
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

# 1. word.txt 파일로 부터 단어를 읽어들임
content = open("word.txt", "r")
# with open('data/word.txt', 'r') as file:
# 방법1
# read_words = file.readlines()
# print(readwords)
# for word in read_words:
#  print(word.strip().rsplit("\n"))  => 맨 오른쪽에 있는 \n을 제거해줌
# 방법2

  # 단어들 출력 
run = content.read()
print(run)

# 2. 제시된 단어 5개까지 타이핑함
print("문자열을 입력하세요")
typed_word = [input() for _ in range(5)]
print("입력하신 단어들은: ", typed_word, "입니다.")


# 3. 리스트 단어를 썩어서, 랜덤하게 하나의 단어를 뽑아서 제시함.
# qs =temp[random.randrange(0,len(temp))]
choiceWord = random.choiceWord(content)
print(choiceWord)

# 4. 타이핑한 단어와 비교함.
# 5. 맞췄을 때와, 틀렸을 때 소리를 구분함.
typed_word = content
if typed_word == content:
    sd = pyglet.resource.media('./assets/good.wav', streaming=False)
    sd.play()
    time.sleep(2)
 
if typed_word != content:
    sd = pyglet.resource.media('./assets/bad.wav', streaming=False)
    sd.play()
    time.sleep(2)

# 6. 걸린시간, 맞춘 갯수 출력



# 7. 3개 이상 맞추면 합격, 2개 이하면 불합격
