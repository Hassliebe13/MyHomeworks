from pprint import pprint
from dataset.marvel import full_dict

marvel_phases = {
    1: "Первая фаза",
    2: "Вторая фаза",
    3: "Третья фаза",
    4: "Четвертая фаза",
    5: "Пятая фаза",
    6: "Шестая фаза",
}

for phase, name in marvel_phases.items():
    print(f"{phase}: {name}")
pass
user_phase = input("Введите номер фазы для выбора: ")
pass

for film in full_dict.items():
    for stage in film:
        if "stage" == user_phase:
            pprint(stage)
