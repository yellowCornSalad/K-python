# https://wikidocs.net/72
# 파이썬 딕셔너리 자습

# dic이라는 이름의 비어있는 딕셔너리를 만든다.
dic = {}
dic ['dictionary'] = 'A reference book that contains the meaning of words'
dic['python'] = 'Any of various nonvenomous snakes of the world'

# print(dic['dictionary'])

# 포켓용사전
smalldic = {'dictionary' : 'reference', 'python': 'snake'}
# print(smalldic['python'])
print(smalldic)

# 원소 삭제
del smalldic['dictionary']
print(smalldic)