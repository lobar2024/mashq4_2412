# 1) 1–5: son → kvadrat
dict1 = {i: i**2 for i in range(1, 6)}

# 2) so‘z → uzunligi
words = ["apple", "banana", "kiwi"]
dict2 = {word: len(word) for word in words}

# 3) faqat juft sonlar: son → kub
nums = [1, 2, 3, 4, 5]
dict3 = {i: i**3 for i in nums if i % 2 == 0}

# 4) talaba → ism uzunligi
students = ["Ali", "Vali", "Guli"]
dict4 = {student: len(student) for student in students}

print(dict1, dict2, dict3, dict4)
