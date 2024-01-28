# TODO Напишите функцию find_common_participants
def find_common_participants(p1, p2, argument=","):
    p1 = set(p1.split(argument))
    p2 = set(p2.split(argument))
    return sorted(set.intersection(p1, p2))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
result = find_common_participants(participants_first_group, participants_second_group, "|")
print(result)
