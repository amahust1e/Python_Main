import json
FILENAME = "input.json"

# TODO решите задачу
def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)
    result = sum([i['score'] * i['weight'] for i in json_data])
    return round(result, 3)

print(task())
