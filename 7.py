"""
7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
"""


def calculator_prog(arg_1, operation, arg_2):
    if operation == "*":
        sum = arg_1 * arg_2
        print("multiplication result: {0} * {1} = {2}".format(arg_1, arg_2, sum))
    elif operation == "/":
        if arg_2 != 0:
            sum = arg_1 / arg_2
            print("division result: {0} / {1} = {2}".format(arg_1, arg_2, sum))
        else:
            print("division by zero.")
    elif operation == "+":
        sum = arg_1 + arg_2
        print("addition result: {0} + {1} = {2}".format(arg_1, arg_2, sum))
    elif operation == "-":
        sum = arg_1 - arg_2
        print("the result of subtraction : {0} - {1} = {2}".format(arg_1, arg_2, sum))
    else:
        print("entered an incorrect operation: <<{0}>>".format(operation))


while True:
    try:
        arg_1 = float(input("enter the first argument: "))
        operation = input("enter one of the action << *, / , + , - >>: ")
        arg_2 = float(input("enter the second argument: "))

        calculator_prog(arg_1, operation, arg_2)

        print("*" * 57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)
        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")
