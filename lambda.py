def fee_generator(fees):
    return lambda adjustment: f"₦{adjustment + fees}"

primary_fee = fee_generator(5000)
secondary_fee = fee_generator(10000)

print("Primary adjusted fee:", primary_fee(50000))
print("Secondary adjusted fee:", secondary_fee(50000))