from functools import reduce

sonlar = [10,20,30,40]

yigindi = reduce(lambda a,b: a+b,sonlar)

ortacha = yigindi/len(sonlar)

print(ortacha)