# TODO импортировать необходимые модули
import csv
import json
#Создаем переменные с указанными для них путями
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None: #создаем функцию для конвертации наших файлов
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r') as file: #открываем входящий .csv файл в формате чтения под именем объекта файла file
        reader_dict = csv.DictReader(file, delimiter=',') #дисериализуем информацию из .csv файлового объекта file методом DictReader, возвращая каждую строку в виде типа данных `OrderedDict` из модуля `collections`
        data = list(reader_dict)  # преобразуем типа данных `OrderedDict` в список состоящий из словарей таблицы из .csv файла
    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding="utf-8") as result: #открываем исходящий .json файл в формате записи под именем файлового объекта result в кодировке utf-8
        json.dump(data, result, indent=4, ensure_ascii=False) #сериализуем в .json наш список словарей из дисериализованного .csv файла по требованиям, указанным в задании с учетом, чтобы наша информация была в кодировке utf-8 на случай наличия в таблице русских букв
if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
