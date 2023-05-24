from colorama import Fore, Back, Style

def get_employees():
    superman = input("Хотители вы у нас работать Да/Нет: ")
    if superman == "Да":
        print(Fore.GREEN + Back.YELLOW + "поздравляю вы приняты")
    elif superman == "Нет":
        print("поздравляю вы неприняты")
    else:
        print(Fore.BLACK + Back.RED + "Попробуйте еще раз")

if __name__ == '__main__':
    get_employees()