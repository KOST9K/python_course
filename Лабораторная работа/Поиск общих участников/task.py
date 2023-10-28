# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, splitter=','):
    first_group_splited = first_group.split(splitter)
    second_group_splited = second_group.split(splitter)
    common_participants = list(set(first_group_splited).intersection(second_group_splited))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
