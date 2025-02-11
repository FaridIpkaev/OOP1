# def spisok_files(*file_names):
#     with open("new_file.txt", "a+") as new_file:  # Открываем файл для добавления
#         z = sorted(file_names, key=lambda x: sum(1 for line in open(x)), reverse=False)
#         for n in z:
#             new_file.write(n + '\n')
#             line_count = sum(1 for line in open(n))  # Подсчитываем количество строк
#             z = str(line_count)
#             new_file.write(z + '\n')
#             with open(n) as file:
#                 for line in file:
#                     new_file.write(line)  # Добавляем содержимое файла
#                 new_file.write('\n')
#     return
# spisok_files('1.txt', '2.txt', '3.txt')   


def spisokfiles(*filenames):
    sortedfiles = sorted(filenames, key=lambda x: sum(1 for _ in open(x, encoding="utf-8")), reverse=False)

    with open("new_file.txt", "w", encoding="utf-8") as new_file:
        for file_name in sortedfiles:
            with open(file_name, encoding="utf-8") as file:
                lines = file.readlines()  # Читаем все строки один раз
                line_count = len(lines)  # Подсчитываем строки

            new_file.write(file_name + '\n')
            new_file.write(str(line_count) + '\n')

            with open(file_name, encoding="utf-8") as file:
                new_file.writelines(file)  # Копируем содержимое файла

            new_file.write('\n')  # Добавляем пустую строку между файлами
spisokfiles('1.txt', '2.txt', '3.txt')