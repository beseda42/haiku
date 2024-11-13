from functions import check_file_haiku
from functions import print_haiku

check_file_haiku("haiku.txt", "test_haiku.txt")

print("Вывести каждое хайку в виде трехстишья? Если согласны, напишите Да")
user_input = input()
if user_input.casefold() == "Да".casefold():
    print_haiku("test_haiku.txt")