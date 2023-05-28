from colorama import Fore, Back, Style
from datetime import datetime
from my_package.salary import calculate_salary as kash
from my_package.people import get_employees


current_datetime = datetime.now().date()


print(current_datetime)

kash()
get_employees()










