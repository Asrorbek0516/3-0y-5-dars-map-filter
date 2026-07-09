ismlar = ["ali", "jasur", "iqbol", "bek"]

katta= map(lambda x: x.upper(),ismlar)

new = list(filter(lambda x: len(x)>4,katta))

print(new)