#Date: 14-9-2026
#Exercise_1
def multiply(a, b):
    return a * b
product = multiply(4, 5)
print(product) 


#Exercise_2
def describe_city(city_name, country_name="USA"):
    print(f"{city_name} is a city in {country_name}.")
describe_city("New York")
describe_city("Chicago")
describe_city("Otukpo", "Nigeria")


#Exercise_3
def sum_all(*args):
    return sum(args)
result = sum_all(10, 5, 8, 2, 5)
print(result)



#Exercise_4
def check_even(n):
    return n % 2 == 0

is_even = lambda n: n % 2 == 0 
print(is_even(20))
print(is_even(15))
