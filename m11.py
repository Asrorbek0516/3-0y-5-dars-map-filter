words = ["men", "salom", "yo", "dastur"]

result = list(filter(lambda x: len(x) % 2 == 1, words))

print(result)
