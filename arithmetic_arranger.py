
#Error function
def error_function(n1, op, n2):
    try:
        int(n1)
        int(n2)
    except:
        return "Error: Numbers must only contain digits."

    try:
        if len(n1) > 4 or len(n2) > 4:
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."

    try:
        if op != "+" and op != "-":
            raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."
    return True

#Function
def arithmetic_arranger(problems):
    side_space = "    "
    line1 = line2 = line3 = line4 = ""
    st = True

    try:
        if len(problems) > 5:
            raise BaseException
    except:
        return "Error: Too many problems."

    for prob in problems:
        div_problems = prob.split()
        n1 = str(div_problems[0])
        op = str(div_problems[1])
        n2 = str(div_problems[2])

        exp = error_function(n1, op, n2)

        if exp != True:
            return exp

        no1 = int(n1)
        no2 = int(n2)

        space = max(len(n1), len(n2))

        if st == True:
            line1 += n1.rjust(space +2)
            line2 += op + " " + n2.rjust(space)
            line3 += "-" * (space +2)

            if op == "+":
                line4 += str(no1 + no2).rjust(space + 2)
            else:
                line4 += str(no1 + no2).rjust(space + 2)
            st = False
        else:
            line1 += n1.rjust(space + 6)
            line2 += op.rjust(5) + ' ' + n2.rjust(space)
            line3 += side_space + '-' * (space + 2)

            if op == "+":
                    line4 += side_space + str(no1 + no2).rjust(space + 2)
            else:
                    line4 += side_space + str(no1 - no2).rjust(space + 2)

    return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 