#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, mul, sub, div
    import sys

    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = sys.argv[2]
    operators = ['+', '-', '*', '/']
    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print(f"{sys.argv[1]} {op} {sys.argv[3]} = {int(sys.argv[1])} {op} {int(sys.argv[3])}")
