def linear_equ_func():
    equ_format = "a(bx + c) + d = e - fx"
    equ = input(f"Enter your linear equation in this format: {equ_format}: \n")

    # equ = '2(4x + 3) + 6 = 24 - 4x'
    print(f"The equation is: {equ}\n")

    # Splitting the equation into components.
    equ_parts = equ.split(" ")
    print(equ_parts)

    a = float(equ_parts[0].split("(")[0])
    b = float(equ_parts[0].split("(")[1].split("x")[0])
    c = float(equ_parts[2].split(")")[0])
    d = float(equ_parts[4])
    e = float(equ_parts[6])
    f = float(equ_parts[8].split("x")[0])
    c_sign = equ_parts[1]
    d_sign = equ_parts[3]
    f_sign = equ_parts[7]

    print("First, expand the bracket...")
    equ1 = f"({b}x * {a}) {c_sign} ({c} * {a}) {d_sign} {d} = {e} {f_sign} {f}x\n"
    print(equ1)

    eval1 = b * a
    eval2 = eval(f"{a}*{c_sign}{c}")

    if eval2 >= 0:

        print("Solve and remove the bracket...")
        equ2 = f"{eval1}x + {eval2} {d_sign} {d} = {e} {f_sign} {f}x\n"
        print(equ2)

        eval3 = eval(f"{eval2} {d_sign} {d}")
        if eval3 >= 0:

            print("Simplify the equation...")
            equ3 = f"{eval1}x + {eval3} = {e} {f_sign} {f}x\n"
            print(equ3)

            if f_sign == "+":

                print("Move like terms to same side...")
                equ4 = f"{eval1}x - {f}x = {e} - {eval3}\n"
                print(equ4)

                eval4 = eval(f"{eval1} - {f}")
                eval5 = eval(f"{e} - {eval3}")

                print("Further simplify the equation...")
                equ5 = f"{eval4}x = {eval5}\n"
                print(equ5)

                print(f"Divide both side by {eval4}")
                equ6 = f"{eval4}x / {eval4} = {eval5} / {eval4}\n"
                print(equ6)

                print("Finally, the answer is...")
                equ7 = f"x = " + str(eval5 / eval4)
                print(equ7)

            else:
                print("Move like terms to same side...")
                equ4 = f"{eval1}x + {f}x = {e} - {eval3}\n"
                print(equ4)

                eval4 = eval(f"{eval1} + {f}")
                eval5 = eval(f"{e} - {eval3}")

                print("Further simplify the equation...")
                equ5 = f"{eval4}x = {eval5}\n"
                print(equ5)

                print(f"Divide both side by {eval4}")
                equ6 = f"{eval4}x / {eval4} = {eval5} / {eval4}\n"
                print(equ6)

                print("Finally the answer is...")
                equ7 = f"x = " + str(eval5 / eval4)
                print(equ7)

        else:
            eval3 = eval3 * -1

            print("Simplify the equation...")
            equ3 = f"{eval1}x - {eval3} = {e} {f_sign} {f}x\n"
            print(equ3)

            if f_sign == "+":
                print("Move like terms to same side...")
                equ4 = f"{eval1}x - {f}x = {e} + {eval3}\n"
                print(equ4)

                eval4 = eval(f"{eval1} - {f}")
                eval5 = eval(f"{e} + {eval3}")

                print("Further simplify the equation...")
                equ5 = f"{eval4}x = {eval5}\n"
                print(equ5)

                print(f"Divide both side by {eval4}")
                equ6 = f"{eval4}x / {eval4} = {eval5} / {eval4}\n"
                print(equ6)

                print("Finally, the answer is...")
                equ7 = f"x = " + str(eval5 / eval4)
                print(equ7)

            else:
                print("Move like terms to same side...")
                equ4 = f"{eval1}x + {f}x = {e} + {eval3}\n"
                print(equ4)

                eval4 = eval(f"{eval1} + {f}")
                eval5 = eval(f"{e} + {eval3}")

                print("Further simplify the equation...")
                equ5 = f"{eval4}x = {eval5}\n"
                print(equ5)

                print(f"Divide both side by {eval4}")
                equ6 = f"{eval4}x / {eval4} = {eval5} / {eval4}\n"
                print(equ6)

                print("Finally, the answer is...")
                equ7 = f"x = " + str(eval5 / eval4)
                print(equ7)

    else:
        eval2 = eval2 * -1

        print("Solve and remove the bracket...")
        equ2 = f"{a*b}x - {eval2} {d_sign} {d} = {e} {f_sign} {f}x\n"
        print(equ2)

        eval3 = eval(f"-{eval2} {d_sign} {d}")
        if eval3 >= 0:

            print("Simplify the equation...")
            equ3 = f"{eval1}x + {eval3} = {e} {f_sign} {f}x\n"
            print(equ3)

            if f_sign == "+":
                print("Move like terms to same side...")
                equ4 = f"{eval1}x - {f}x = {e} - {eval3}\n"
                print(equ4)

                eval4 = eval(f"{eval1} - {f}")
                eval5 = eval(f"{e} - {eval3}")

                print("Further simplify the equation...")
                equ5 = f"{eval4}x = {eval5}\n"
                print(equ5)

                print(f"Divide both side by {eval4}")
                equ6 = f"{eval4}x / {eval4} = {eval5} / {eval4}\n"
                print(equ6)

                print("Finally, the answer is...")
                equ7 = f"x = " + str(eval5 / eval4)
                print(equ7)

            else:
                print("Move like terms to same side...")
                equ4 = f"{eval1}x + {f}x = {e} - {eval3}\n"
                print(equ4)

                eval4 = eval(f"{eval1} + {f}")
                eval5 = eval(f"{e} - {eval3}")

                print("Further simplify the equation...")
                equ5 = f"{eval4}x = {eval5}\n"
                print(equ5)

                print(f"Divide both side by {eval4}")
                equ6 = f"{eval4}x / {eval4} = {eval5} / {eval4}\n"
                print(equ6)

                print("Finally, the answer is...")
                equ7 = f"x = " + str(eval5 / eval4)
                print(equ7)

        else:
            eval3 = eval3 * -1

            print("Simplify the equation...")
            equ3 = f"{eval1}x - {eval3} = {e} {f_sign} {f}x\n"
            print(equ3)

            if f_sign == "+":

                print("Move like terms to same side...")
                equ4 = f"{eval1}x - {f}x = {e} + {eval3}\n"
                print(equ4)

                eval4 = eval(f"{eval1} - {f}")
                eval5 = eval(f"{e} + {eval3}")

                print("Further simplify the equation...")
                equ5 = f"{eval4}x = {eval5}\n"
                print(equ5)

                print(f"Divide both side by {eval4}")
                equ6 = f"{eval4}x / {eval4} = {eval5} / {eval4}\n"
                print(equ6)

                print("Finally, the answer is...")
                equ7 = f"x = " + str(eval5 / eval4)
                print(equ7)

            else:
                print("Move like terms to same side...")
                equ4 = f"{eval1}x + {f}x = {e} + {eval3}\n"
                print(equ4)

                eval4 = eval(f"{eval1} + {f}")
                eval5 = eval(f"{e} + {eval3}")

                print("Further simplify the equation...")
                equ5 = f"{eval4}x = {eval5}\n"
                print(equ5)

                print(f"Divide both side by {eval4}")
                equ6 = f"{eval4}x / {eval4} = {eval5} / {eval4}\n"
                print(equ6)

                print("Finally, the answer is...")
                equ7 = f"x = " + str(eval5 / eval4)
                print(equ7)
    return eval5 / eval4


solve = linear_equ_func()
