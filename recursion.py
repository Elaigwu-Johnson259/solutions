# def calculate_total(score):
#     if score == 0:
#         return 0
#     else:
#         return score + calculate_total(score - 1)

# print(calculate_total(5))


calculate_fee = lambda tuition, registration: f"₦{tuition + registration}"
print(calculate_fee(150000, 25000))

student_average = lambda name, maths, english, science: f"Student: {name}\nTotal: {maths + english + science}\nAverage: {round(((maths + english + science) / 3), 2)}"
print(student_average("Johnson", 80, 75, 90))
