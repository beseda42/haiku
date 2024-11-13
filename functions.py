from collections import Counter
import re
import sys
from pathlib import Path

def check_file_haiku(input_path, output_path):
    '''
    Функция, проверяющая трехстишья, у которых строки разделены /,
    а сами между собой они разделены разными строками, на принадлежность к
    хайку - жанру поэзии, в котором слоги в строках чередуются как 5/7/5

    :param input_path: входной файл
    :param output_path: файл для вывода
    :return:
    '''

    def count_syllable(line):
        '''
        :param line: строка
        :return: количество слогов (гласных) в line
        '''
        return sum(Counter(line.lower())[char] for char in "аеёиоуыэюя")

    def check_syllable(line_number, given_syllable):
        '''
        :param line_number: номер строки
        :param given_syllable: количество слогов в строке
        :return: совпадает ли текущее количество слогов в строке с необходимым
        '''
        requested = 0
        if line_number == 1 or line_number == 3:
            requested = 5
        if line_number == 2:
            requested = 7

        if given_syllable == requested:
            if line_number == 3:
                print ("Хайку!")
            return True
        else:
            print (f"Не хайку. В {line_number} строке слогов не {requested}, а {given_syllable}")
            return False

    def check_haiku(text):
        '''
        Проверяет, является ли строка text хайку

        :param text: одна строка в файле (в идеале - трехстишье, разделенное /)
        '''

        #В хайку должно быть ровно 3 строки
        if text.count('/') != 2:
            print ("Не хайку. Должно быть 3 строки.")
            return

        #Делим текст на строки
        lines = re.split(r'\s*/\s*', text)

        #Проверяем строки на слоги
        for i in range(3):
            if check_syllable(i + 1, count_syllable(lines[i])):
                continue
            else:
                break

    #сохранение обычный поток вывода
    og_stdout = sys.stdout

    #открытие input_file на чтение и output_file на запись
    with open (input_path, 'r', encoding='utf-8') as input_file, open (output_path, 'w', encoding='utf-8') as output_file:
        #изменение поток вывода для прямой записи в output_file
        sys.stdout = output_file

        #проверка всех строк на хайку
        for line in input_file:
            print(line.strip())
            check_haiku(line.strip())
            print ()

    #возвращение обычного потока вывода
    sys.stdout = og_stdout

def print_haiku(input_path):
    '''
    Выводит в консоль хайку в виде трехстишья

    :param input_path: входной файл
    '''
    with open (input_path, 'r', encoding='utf-8') as file:
        prev_line = ""
        for line in file:
            if line.strip() == "Хайку!":
                for lines in re.split(r'\s*/\s*', prev_line):
                    print (lines)
                print()
            prev_line = line.strip()



