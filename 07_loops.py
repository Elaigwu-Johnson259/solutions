#Date: 11-9-2026
#Exercise_1
total = 0
numbers = range(51)
for num in numbers:
    total = total + num 
print(total)



# Exercise_2
count = 1
while count <= 15:
    if count % 2 == 0:
        count += 1
        continue
    else:
        print(count)
    count += 1



#Exercise_3
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
for name in names:
    if name == "Charlie":
        print(name)
        break


# Exercise_4
list_com = [len(name) for name in names]
print(list_com)
