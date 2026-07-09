sonlar = [10, 15, 20, 30, 45]

numbers = list(filter(lambda x: x%3==0 and x%5==0 ,sonlar))

print(numbers)