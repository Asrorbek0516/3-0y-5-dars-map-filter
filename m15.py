students = [("Ali", 90), ("Vali", 78), ("Zara", 95)]

bahosi_yuqori = filter(lambda x: x[1]>85,students)

ismi_ozgartir = list(map(lambda x: x[0].upper(),bahosi_yuqori))

print(ismi_ozgartir)