def calculator() :
    operator = input("Choose the operator (+, -, /, *, **, +-/***) : ")

    if operator == "+" :
        v1 = int(input("First Value Enter : "))
        v2 = int(input("Second Value Enter : "))
        result = v1 + v2
        print("## CALCULATOR %d %s %d = %d ##" % (v1, operator, v2, result))
    elif operator == "-" :
        v1 = int(input("First Value Enter : "))
        v2 = int(input("Second Value Enter : "))
        result = v1 - v2
        print("## CALCULATOR %d %s %d = %d ##" % (v1, operator, v2, result))
    elif operator == "*" :
        v1 = int(input("First Value Enter : "))
        v2 = int(input("Second Value Enter : "))
        result = v1 * v2
        print("## CALCULATOR %d %s %d = %d ##" % (v1, operator, v2, result))
    elif operator == "/" :
        v1 = int(input("First Value Enter : "))
        v2 = int(input("Second Value Enter : "))
        result = v1 / v2
        print("## CALCULATOR %d %s %d = %.1lf ##" % (v1, operator, v2, result))
    elif operator == "**" :
        v1 = int(input("First Value Enter : "))
        v2 = int(input("Second Value Enter : "))
        result = v1 ** v2
        print("## CALCULATOR %d %s %d = %d ##" % (v1, operator, v2, result))
    elif operator == "+-/***" :
        var = input("Input Mathematical Expression : ")
        result = eval(var)
        print("%s result → %.1lf" % (var, result))
    else :
        print("... Error.")
        print("... Re try.")

print("## +-/*** : Mathematical Expression , ", end = "")
print("Other Operator : Elementary Arithmetic ##")
"""print(calculator())"""