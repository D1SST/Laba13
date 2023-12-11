# Определить количество пассажиров на борту в возрастном интервале
# средний возраст +- 10 позиций и сколько из них выжило

import csv

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            data.append(row)
    return headers, data

def age_interval_survival_count(data, age, margin):
    count_total = 0
    count_survived = 0

    for row in data:
        if row[4] != '' and float(row[4]) - margin <= age <= float(row[4]) + margin:
            count_total += 1
            if row[0] == '1':
                count_survived += 1

    return count_total, count_survived

def main():
    file_path = 'titanic.csv'
    headers, data = read_csv(file_path)

    age_to_check = 30  # Возраст, для которого проверяется интервал
    age_margin = 10  # +- для интервала возраста

    count_total, count_survived = age_interval_survival_count(data, age_to_check, age_margin)

    print(f'Возрастной интервал {age_to_check - age_margin} - {age_to_check + age_margin}:')
    print(f'Количество пассажиров на борту при заданном возрастном интервале: {count_total}')
    print(f'Из них выжило: {count_survived}')

if __name__ == "__main__":
    main()
