import re


def get_request_numbers():  # Возвращает общее количество запросов
    with open(r'hometask_7\access.log', 'r') as f:
        counter = -1
        for lines in f:
            counter += 1
        print('Задание 1. Количество запросов -', counter)


def unique_ips():  # Возвращает количество уникальных запросов
    with open(r'hometask_7\access.log', 'r') as f:
        pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ip_list = set()
        for line in f:
            if len(line) <= 1:
                continue
            else:
                result = re.search(pattern, line)
                ip_list.add(result.group(0))
        print('Задание 2. Количество уникальных ip адресов -', len(ip_list))


def browser_counter():  # Считает, какие браузеры обращались и сколько раз
    with open(r'hometask_7\access.log', 'r') as f:
        counter = {
            'Chrome': 0,
            'Opera': 0,
            'Firefox': 0,
            'Safari': 0,
            'Edg': 0,
        }
        for line in f:
            agent = line[-35:-6]
            for keys in counter.keys():
                if keys in agent:
                    counter[keys] += 1
        print('Задание 3 и 4. Какие браузеры обращались и сколько раз:')
        for keys, values in counter.items():
            print(keys, '-', values)


if __name__ == '__main__':
    get_request_numbers()
    unique_ips()
    browser_counter()
