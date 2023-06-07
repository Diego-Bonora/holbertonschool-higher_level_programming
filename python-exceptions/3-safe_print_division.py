#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        num = a / b
    except Exception:
        num = None
    finally:
        return num
