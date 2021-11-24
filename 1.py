"""
1. Створити цикл від 0 до ... (вводиться користувачем).
   В циклі створити умову, яка буде виводити поточне значення,
   якщо остача від ділення на 17 дорівнює 0.
"""


def range_number(num):
    if int(num) > 0:
        list_random = [y for y in range(0, num) if y % 17 == 0]
        return list_random
    else:
        print("value is negative, enter a positive value ")


while True:
    try:
        arg_1 = int(input("enter an integer value greater than zero : "))
        print("the current value is a multiple of 17 -> {0}".format(range_number(arg_1)))

        print("*" * 57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)
        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")