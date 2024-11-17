# converter/utils.py

def decimal_to_binary(decimal_value):
    return bin(decimal_value)[2:]

def decimal_to_octal(decimal_value):
    return oct(decimal_value)[2:]

def decimal_to_hexadecimal(decimal_value):
    return hex(decimal_value)[2:].upper()

def binary_to_decimal(binary_value):
    return int(binary_value, 2)

def octal_to_decimal(octal_value):
    return int(octal_value, 8)

def hexadecimal_to_decimal(hexadecimal_value):
    return int(hexadecimal_value, 16)
