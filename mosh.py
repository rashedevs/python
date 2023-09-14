# patient_name = "John Smith"
# patient_age = 20
# is_new = True
# print(patient_name, patient_age, is_new)

# name = input("give some input here ")
# print("Hello " + name)

# birth_year = input("Enter your birth year ")
# age = 2023 - int(birth_year)
# print("You are " + str(age) + " years old")

# first = float(input("Enter first: "))
# second = float(input("Enter second: "))
# sum = first + second
# print(sum)

# print(10 / 3)  # division
# print(10 // 3)  # floor round
# print(10 % 3)  # modulas
# print(10**3)  # exponential

# temp = 10
# if temp > 30:
#     print("It's a hot day")
# elif temp > 20:
#     print("It's a cool day")
# elif temp > 10:
#     print("It's a bit cold day")
# else:
#     print("It's a cold day")
# print("Done")

# Exercise for unit converter

# weight = int(input("Weight: "))
# unit = input("(K)g or (L)bs: ")

# if unit.upper() == "L":
#     converted = weight * 0.45
#     print("Weight in Kgs: " + str(converted))
# else:
#     converted = weight / 0.45
#     print("Weight in Lbs: " + str(converted))

# while loop: '_' is used with 00 for more readable code.

i = 1
while i <= 10:
    # while i <= 1_000:
    print(i * "*")
    i += 1

# List

# names = ["John", "Bob", "Mosh", "Sam", "Mary"]
# names[0] = "Jon"
# print(names[0:3])

# List Methods:

# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)
# numbers.insert(2, "R")
# numbers.remove(3)
# numbers.clear()
# print(6 in numbers)
# print(len(numbers))

# For loops:

# numbers = [1, 2, 3, 4, 5]
# for x in numbers:
#     print(x)

# Range:
# numbers = range(5, 10, 2)  # (0 to 4) // Here (from 5,to 10(excluded),step 2)
# for x in range(5):
#     print(x)

# Tuple: tuples are immutable/unchangable
numbers = (1, 2, 3, 3, 4, 5)
print(numbers.count(3))
