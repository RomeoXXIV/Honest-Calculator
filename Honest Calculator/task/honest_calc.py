# write your code here
msg_ = ["Enter an equation",
        "Do you even know what numbers are? Stay focused!",
        "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "Yeah... division by zero. Smart move...",
        "Do you want to store the result? (y / n):",
        "Do you want to continue calculations? (y / n):",
        " ... lazy",
        " ... very lazy",
        " ... very, very lazy",
        "You are",
        "Are you sure? It is only one digit! (y / n)",
        "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)"]

memory = 0


def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_[7]
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)


while True:
    calc = input(msg_[0])
    x, oper, y = calc.split()

    x = memory if x == "M" else x
    y = memory if y == "M" else y

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_[1])
        continue
    else:
        if oper in ["+", "-", "*", "/"]:
            check(x, y, oper)
            if oper == "+":
                result = x + y
            elif oper == "-":
                result = x - y
            elif oper == "*":
                result = x * y
            elif oper == "/":
                try:
                    result = x / y
                except ZeroDivisionError:
                    print(msg_[3])
                    continue
        else:
            print(msg_[2])
            continue

    print(result)

    while True:
        answer = input(msg_[4])
        if answer == "y":
            if is_one_digit(result):
                msg_index = 10
                while True:
                    answer = input(msg_[msg_index])
                    if answer == "y":
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        else:
                            memory = result
                            break
                    elif answer == "n":
                        break
                    else:
                        continue
            else:
                memory = result
            break
        elif answer == "n":
            break
        elif answer != "n":
            continue

    while True:
        answer = input(msg_[5])
        if answer == "y":
            continue_calculations = True
            break
        elif answer == "n":
            continue_calculations = False
            break
        else:
            continue

    if continue_calculations:
        continue
    else:
        break
