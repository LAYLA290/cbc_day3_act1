numbers = [2, 3]
numero = [2]

is_greater = numero > numbers
print(is_greater)

total = sum(numbers)
product = 1
for num in numbers:
    product *= num

calculations = [total, product]
calculations.insert(1, max(numbers))

average = total / len(numbers)
calculations.append(average)

squares_list = [num ** 2 for num in numbers]
calculations.extend(squares_list)

calculations.remove(min(calculations))

print("Final Results:", calculations)
