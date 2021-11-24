"""
6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi

   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:

-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр

-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)

-  якщо довжина бульше 50 - > ваша фантазiя
"""


def text_length(text):
    if len(text) in range(30, 50):
        char_list = []
        for char in text:
            if char.isdigit():
                char_list.append(char)
        print("number of letters in a line -> {0}".format(len(char_list)))

        num_list = []
        for num in text:
            if num.isalpha():
                num_list.append(num)
        print("number of digits in a line -> {0}".format(len(num_list)))

    elif len(text) <= 30:
        num_list = []
        num_text = ""
        for char in text:
            if char.isdigit():
                num_text += char
            else:
                if num_text != "":
                    num_list.append(int(num_text))
                    num_text = ""
                    print(num_text)
        if num_text != "":
            num_list.append(int(num_text))
        print("the sum of all numbers in a row -> {0}".format(sum(num_list)))

        char_text = ""
        for char in text:
            if char.isalpha():
                char_text += char
        print("string without numbers -> {0}".format(char_text))

    elif len(text) >= 50:
        ascii_list=[]
        for i in text:
            ascii_list.append(ord(i))
        print("the sum of all characters in the ASCII table -> {0}".format(sum(ascii_list)))

    else:
        print("<<*****>>")


while True:
    try:
        test = "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345"
        str_text = input("enter any set of numbers and letters: ")
        text_length(str_text)

        print("*" * 57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)
        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")
