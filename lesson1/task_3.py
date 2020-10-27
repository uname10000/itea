n = 100

found = False
out_msg = ''
for i in range(1, n + 1):
    if i % 3 == 0:
        out_msg += 'Fizz '
        found = True
    if i % 5 == 0:
        out_msg += 'Buzz '
        found = True
    if i % 15 == 0:
        out_msg += 'FizzBuzz'
        found = True

    if not found:
        print(i)
    else:
        print(out_msg)

    found = False
    out_msg = ''
