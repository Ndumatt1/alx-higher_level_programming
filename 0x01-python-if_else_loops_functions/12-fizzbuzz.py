#!/usr/bin/python3
number = 1
while number <= 100:
    if number % 3 == 0:
        #continue
        print('Fizz ', end="")
    elif number % 5 == 0:
        #continue
        print('Buzz ', end="")
    elif number % 3 == 0 and number % 5 == 0:
        #continue
        print('FizzBuzz ', end="")
    else:
        print("{} ".format(number), end="")
    number = number + 1
