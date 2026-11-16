def calculate_total(score):
    if score == 0:
        return 0
    else:
        return score + calculate_total(score - 1)

print(calculate_total(5))

