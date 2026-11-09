def calculate_bill(*bills):
    total = 0
    for bill in bills:
        total = total + bill
    print(f"Total bill: ₦{total}")

calculate_bill(500, 400, 600)
calculate_bill(1000, 1500, 1000)
calculate_bill(2000, 3000, 5000)