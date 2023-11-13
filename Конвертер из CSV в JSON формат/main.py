# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(splitter=',', row_splitter='\n') -> None:
    with open(INPUT_FILENAME, newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=splitter)# TODO считать содержимое csv файла
        data = []
        for item in csv_reader:
            data.append(item)
            with open(OUTPUT_FILENAME, 'w') as json_file:
                json.dump(data, json_file, indent=4)
      # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
