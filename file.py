def open_read_file(file_name):
    """Функция для вывода содержимого файла
    """
    with open(file_name, encoding='utf-8') as file:
        data = file.read()
        return data

def count_number_of_line(file_name):
    """Функция для подсчета количества строк в файле
    """
    count_line = len(open(file_name, encoding='utf-8').readlines())
    return count_line

def write_new_file():
    """Функция для сортировки исходных файлов и записи содержимого в новый файл
    """
    with open('result_file.txt', 'w', encoding='utf-8') as document:
        for file in files_list_sorted:
            document.write(f'{file.name}\n')
            document.write(f'{str(file.lines)}\n')
            document.write(f'{file.data}\n')

class Files:
    def __init__(self, name, lines, data):
        self.name = name
        self.lines = lines
        self.data = data

file_1 = Files('1.txt', count_number_of_line('1.txt'), open_read_file('1.txt'))
file_2 = Files('2.txt', count_number_of_line('2.txt'), open_read_file('2.txt'))
file_3 = Files('3.txt', count_number_of_line('3.txt'), open_read_file('3.txt'))

files_list = [file_1, file_2, file_3]

from operator import attrgetter

files_list_sorted = sorted(files_list, key=attrgetter('lines'))

write_new_file('')