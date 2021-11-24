"""
2. Користувачем вводиться початковий і кінцевий рік. Створити цикл,
   який виведе всі високосні роки в цьому проміжку (границі включно).
"""


def definition_of_a_leap_year(start_year, end_year):
    if (start_year > 0) and (end_year > 0):
        for year in range(start_year, end_year + 1):
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print("leap years -> {0}".format(year))
    else:
        print("you entered a negative year")


while True:
    try:
        start_year = int(input("enter the start of the year range: "))
        end_year = int(input("eenter the end of the year range: "))
        if (start_year > 0) and (end_year > 0):
            definition_of_a_leap_year(start_year, end_year)
        else:
            continue

        print("*" * 57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)
        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")
