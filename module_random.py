from random import random, uniform, choice, randrange, shuffle, sample
print("# rnadom 모듈")
print("- rnadom() :", random())
print("- uniform() :", uniform(10, 20))
print("- randrange() :", randrange(10))
print("- choice([1,2,3,4,5]) :", choice([1,2,3,4,5]))
print("- shuffle([1,2,3,4,5]) :", shuffle([1,2,3,4,5]))
print("- sample([1,2,3,4,5]) :", sample([1,2,3,4,5], k=2))