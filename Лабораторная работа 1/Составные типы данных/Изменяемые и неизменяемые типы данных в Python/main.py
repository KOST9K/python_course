# TODO исправьте опечатку в слове
fruits = ["яблоко", "банан", "опельсин", "виноград"]
my_string = fruits[2]
new_string = "а" + my_string[1:]
fruits[2] = new_string
print(fruits)
