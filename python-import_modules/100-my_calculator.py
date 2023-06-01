#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calculator
    import sys
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = sys.argv[2]
    if operator == "+":
        operation = calculator.add(int(sys.argv[1]), int(sys.argv[3]))
        print("{} + {} = {}".format(sys.argv[1], sys.argv[3], operation))
    elif operator == "-":
        operation = calculator.sub(int(sys.argv[1]), int(sys.argv[3]))
        print("{} - {} = {}".format(sys.argv[1], sys.argv[3], operation))
    elif operator == "*":
        operation = calculator.mul(int(sys.argv[1]), int(sys.argv[3]))
        print("{} * {} = {}".format(sys.argv[1], sys.argv[3], operation))
    elif operator == "/":
        operation = calculator.div(int(sys.argv[1]), int(sys.argv[3]))
        print("{} / {} = {}".format(sys.argv[1], sys.argv[3], operation))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
