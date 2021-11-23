"""
3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12),
   яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)
"""


def season(month):
    if month == 12 or month == month in range(1, 2 + 1):
        print("Winter")
    elif month == month in range(3, 5 + 1):
        print("Spring")
    elif month == month in range(6, 8 + 1):
        print("Summer")
    elif month == month in range(9, 11 + 1):
        print("Autumn")
    else:
        print("you entered an invalid month of the year.")


while True:
    try:
        arg_1 = int(input("enter the month of the year: "))
        if (arg_1 > 0) and (arg_1 <= 12):
            season(arg_1)
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
