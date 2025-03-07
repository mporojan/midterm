import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

for i in range(len(random_numbers)):
    if random_numbers[i] > 80:
        random_numbers[i] = -random_numbers[i]
    elif random_numbers[i] < 40:
        number_str = str(random_numbers[i])

        sum_of_digits = 0
        for digit in number_str:
            sum_of_digits += int(digit)

        random_numbers[i] = sum_of_digits

print(random_numbers)
