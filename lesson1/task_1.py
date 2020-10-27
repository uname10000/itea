numbers = int(input('Enter numbers: '))

list_of_numbers = list(range(0, numbers + 1))

# print(list_of_numbers)
for number in list_of_numbers:
    if number % 2 == 0:
        print(str(number))