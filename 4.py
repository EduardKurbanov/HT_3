"""
4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат.
   Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат.
   Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3
"""


def fun_1():
    number_fun_1 = "1"
    num_1 = 1
    print("hi i function №{0}".format(int(number_fun_1)))
    return num_1


def fun_2():
    number_fun_2 = "2"
    num_2 = 1
    print("hi i function №{0}".format(int(number_fun_2)))
    return num_2


def fun_3():
    number_fun_3 = "3"
    num_3 = 1
    print("hi i function №{0}".format(int(number_fun_3)))
    return number_fun_3 and num_3


def fun_4():
    number_fun_4 = "4"
    num_4 = 1
    print("hello i am a function №{0} processing functions №1, №2, №3")
    sum_fun = num_4 + fun_1() + fun_2() + fun_3()
    print("i function {0} counting the sum of the functions of us {1}".format(number_fun_4, sum_fun))


fun_4()
