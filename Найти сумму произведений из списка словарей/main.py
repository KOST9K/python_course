# TODO решите задачу
import json


def task() -> float:
    with open('input.json', 'r') as input_file:
        data = json.load(input_file)
    mult_sum = sum(item["score"] * item["weight"] for item in data)
    return round(mult_sum, 3)


print(task())
