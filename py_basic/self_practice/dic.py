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
# print(smalldic)

# dictionary => list
family = {'boy':'choi', 'girl':'kim', 'baby':'little'}
# 딕셔너리의 family 키들을 새로운 리스트에 담는다.
print(family.keys())
# family의 값들을 새로운 리스트에 담는다.
print(family.values())

# 딕셔너리에 어떤 키 값들이 존재하는지 유무조사
print('boy' in family) # True
print('five' in family) # False
