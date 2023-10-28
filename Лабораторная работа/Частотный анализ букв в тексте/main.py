# TODO  Напишите функцию count_letters
def count_letters(text):
    letters_dictionary = {}
    for char in text.lower():
        if char.isalpha():
            if letters_dictionary.get(char) is None:
                letters_dictionary[char] = 1
            else:
                letters_dictionary[char] += 1
    return letters_dictionary


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters_dictionary):
    letters_sum = sum(letters_dictionary.values())
    for item in letters_dictionary.items():
        letters_dictionary[item[0]] = item[1] / letters_sum
    return letters_dictionary


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

frequency_dictionary = calculate_frequency(count_letters(main_str))
# TODO Распечатайте в столбик букву и её частоту в тексте
for item in frequency_dictionary.items():
    print(f"{item[0]}: {item[1]:.2f}")
