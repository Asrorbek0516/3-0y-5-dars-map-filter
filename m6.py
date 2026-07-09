from functools import reduce
sonlar = [7, 2, 9, 1, 5]

kichigi = reduce(lambda a,b: a if a<b else b,sonlar)

print(kichigi)