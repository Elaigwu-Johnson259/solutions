def calculate_total(score):
    if score == 0:
        return 0
    else:
        return score + calculate_total(score - 1)

print(calculate_total(5))


calculate_fee = lambda tuition, registration: f"₦{tuition + registration}"
print(calculate_fee(150000, 25000))
