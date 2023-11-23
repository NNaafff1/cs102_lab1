import sys

def calc(a, oper, b):
    # global errors

    if oper == "+":
        return round(a + b, 10)

    if oper == "-":
        return round(a - b, 10)

    if oper == ":" or oper == "/":
        if b == 0:
            raise ZeroDivisionError("--На 0 делить нельзя!--")
        return a / b

    if oper == "*":
        # main()
        return a * b

    if oper == "**":
        return a**b


def main():
    # global errors
    f = 1

    print("Введите выражение через пробел (a + b)")
    var = input().replace(",", ".")

    if var == "stop":
        sys.exit()

    if var.count(" ") != 2:
        raise TypeError("--Вы не использовали пробелы или их слишком много!--")
    a, oper, b = var.split()

    try:
        a, b = float(a), float(b)
    except TypeError:
        f = 0
        # print('Ops! ... \n Incorrect arguments \n Please wait 2 seconds and try again.')
        # errors += 1
    if f == 0:
        raise TypeError("--Вы не правильно ввели аргументы!--")
        # time.sleep(1)
        # main()

    operations = ["+", "-", "*", ":", "/", "**"]

    if oper not in operations:

        raise TypeError("--Вы не правильно ввели функцию!--")
        
    print(calc(a, oper, b))


if __name__ == "__main__":
    main()
