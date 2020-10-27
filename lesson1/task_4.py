deposit = 1000
number_of_years = 10
percent = 17


def calculate(dposit, number_of_years, percent):
    deposit_sum = 0
    for i in range(1, number_of_years + 1):
        # print("year: " + str(i))
        deposit_sum += dposit * percent / 100
        # print('deposit: ' + str(deposit_sum))

    return deposit_sum


print('deposit: ' + str(deposit))
print('number_of_years: ' + str(number_of_years))
print('percent: ' + str(percent))
print('- deposit sum is: ' + str(calculate(deposit, number_of_years, percent)))
