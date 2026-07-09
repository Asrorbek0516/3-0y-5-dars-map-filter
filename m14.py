from functools import reduce

sonlar = [1, 2, 3, 4, 5, 6]

juft= list(filter(lambda x: x%2==0,sonlar))

yigindi = reduce(lambda a,b: a+b,juft)

print(yigindi)