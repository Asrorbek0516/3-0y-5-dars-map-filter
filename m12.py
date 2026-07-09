from functools import reduce

sonlar = [1, 2, 3, 4] 

yigindi = reduce(lambda a,b: a+b,sonlar)

print(yigindi**2)

