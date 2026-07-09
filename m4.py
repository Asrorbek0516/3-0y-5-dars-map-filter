numbers = [1.555, 2.349, 3.781]

result = list(map(lambda x: int(x * 100 + 0.5) / 100, numbers))

print(result)