users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
dictionary_ = {"Общее количество": 0, "Уникальные посещения": 0}

dictionary_["Общее количество"] = len(users)
dictionary_["Уникальные посещения"] = len(set(users))

print(dictionary_)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
