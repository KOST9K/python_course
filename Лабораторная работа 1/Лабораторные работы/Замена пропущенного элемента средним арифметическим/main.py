numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

numbers_len = len(numbers)
before_none = numbers[:4]
after_none = numbers[5::]
numbers_sum = sum(before_none) + sum(after_none)
numbers_avg = numbers_sum / numbers_len
numbers[4] = numbers_avg

print("Измененный список:", numbers)
