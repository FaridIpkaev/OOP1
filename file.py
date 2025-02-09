def spisok_files(*file_names):
    with open("new_file.txt", "a+") as new_file:  # Открываем файл для добавления
        z = sorted(file_names, key=lambda x: sum(1 for line in open(x)), reverse=False)
        for n in z:
            new_file.write(n + '\n')
            line_count = sum(1 for line in open(n))  # Подсчитываем количество строк
            z = str(line_count)
            new_file.write(z + '\n')
            with open(n) as file:
                for line in file:
                    new_file.write(line)  # Добавляем содержимое файла
                new_file.write('\n')
    return
spisok_files('1.txt', '2.txt', '3.txt')   

