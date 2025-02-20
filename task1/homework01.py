def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, 'r', encoding='UTF-8') as f:
            for line in f:
                try:
                    name, salary = line.strip().split(',')
                    total += float(salary)
                    count += 1
                except ValueError:
                    print(f"Неправильний формат рядка. Дотримуйтесь формату 'Ім\'я,Зарплата'")

    except FileNotFoundError:
        print('File doesn\'t exist!')
    except Exception as e:
        print(f"Exception has occured: {e}")

    average = total / count if count > 0 else 0
    return total, average