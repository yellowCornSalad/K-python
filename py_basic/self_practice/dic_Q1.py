# https://wikidocs.net/124000
# 연습문제 1: 숫자 읽기(0~9)

def korean_number(num):
    dic = {'0':'영', '1':'일','2':'이', '3':'삼', '4':'사', '5':'오', '6':'육', '7':'칠', '8':'팔', '9':'구'}
    return dic[num]

print(korean_number('3'))