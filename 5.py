"""
5. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;

-  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї), пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.

-  Повиннi опрацювати такi умови:

-  x > y;       вiдповiдь - х бiльше нiж у на z

-  x < y;       вiдповiдь - у бiльше нiж х на z

-  x == y.      вiдповiдь - х дорiвнює z
"""


def comparison_of_values(x, y):
    if x > y:
        z = x - y
        print("x > y, answer - x = {0} greater than y = {1} on {2}".format(x, y, z))
    elif x < y:
        z = y - x
        print("x < y, answer - y = {1} greater than x = {0} on {2}".format(x, y, z))
    elif x == y:
        z = x - y
        print("x == y, answer - x = {0} equals y = {1} on {2}".format(x, y, z))


while True:
    try:
        arg_1 = float(input("enter x: "))
        arg_2 = float(input("enter y: "))

        comparison_of_values(arg_1, arg_2)

        print("*" * 57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)
        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")
