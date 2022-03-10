import pyglet
import time
import random
def make_words():
    with open("data/word.txt","r") as file:
        word = file.read()
        words =word.split("\n")
        num=5
        word_list = random.sample(words,k=num)
        return word_list
def start_game():
    start = input("Ready? Press Enter Key!")
    start_time = time.time() # Enter 누른 뒤 시간 측정
    return start_time
def playing_game():
    word_list = make_words()
    success = 0
    sound_good = pyglet.resource.media("assets/good.wav",streaming =False)
    sound_bad = pyglet.resource.media("assets/bad.wav",streaming =False)
    for times,value in enumerate(word_list):
        print("*Question # ",times +1)
        print(value)
        answer = input("")
        if answer == value:
            sound_good.play()
            print()
            print()
            print("Pass!")
            print()
            success += 1
        else :
            sound_bad.play()
            print()
            print()
            print("Wrong!")
            print()
    time.sleep(1)
    return success
def result_game():
    start_time = start_game()
    success = playing_game()
    if success >= 3:
        print("결과 : 합격")
        print("게임 시간 : %.2f초 정답 개수 : %d" % (time.time()-start_time,success))
    else :
        print("결과 : 불합격")
        print("게임 시간 : %.2f초 정답 개수 : %d" % (time.time()-start_time,success))
def games():
    result_game()
games()