def xor_hex(hex_value_1, hex_value_2):
    """
    inputs: str, str
    output: str
    """
    int_value_1 = int(hex_value_1, 16)
    int_value_2 = int(hex_value_2, 16)
    
    result_int = int_value_1 ^ int_value_2
    
    hex_value = hex(result_int)[2:].zfill(8)
    return hex_value

def hex_to_binary(hex_str, bit):
    """
    input type: str
    output type: binary
    """
    int_value = int(hex_str, 16)  # Convert hex to integer
    binary_value = bin(int_value)[2:].zfill(bit) # Convert integer to binary
    return binary_value

def binary_to_hex(binary_string, bit):
    """
    input type: int list
    output type: str
    """

    int_value = int(binary_string, 2)
    hex_value = hex(int_value)[2:].zfill(bit)
    return hex_value

left = binary_to_hex("11001100000000001100110011111111",32)
f = binary_to_hex("00100011010010101010100110111011",32)

print(hex_to_binary(xor_hex(left,f),32))

# left = int("11001100000000001100110011111111",2)
# f = int("00100011010010101010100110111011",2)
# xor = left ^ f

# print(bin(xor)[2:])