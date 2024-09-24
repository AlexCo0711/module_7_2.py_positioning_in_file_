# Домашнее задание по теме "Позиционирование в файле".
# Цель: Закрепить знания о позиционировании в файле, использовав метод
# tell() файлового объекта. Написать усовершенствованную функцию записи.

#объявление функции custom_write с агументами file_name и strings
def custom_write(file_name, strings):
    # объявление словаря strings_positions
    strings_positions = {}
    # открытие фоайла file_name для записи с использованием кодировки UTF-8
    file = open(file_name, 'w', encoding='utf-8')
    # цикл определения номера строки в индексированном списке strings (enumerate(strings))
    for i,string in enumerate(strings, 1):
        # присвоение значений индексу строки (i), номеру байта (file.tell()) начала строки
        # (для номера байта конца строки эта строка кода прописывается после записи в файл
        # (закоментировано)) ключа строки в словаре strings_positions
        strings_positions[i, file.tell()] = string
        # записm строки (string) в файл
        file.write(string + '\n')
        # strings_positions[i,file.tell()] = string
    # закрытие file
    file.close()
    # возврат функции
    return strings_positions

 # исходные данные
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
# вывод на консоль
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

