def decode_bits(bits):
    bits = bits.strip("0")
    current_bit, bit_array = bits[0], []
        
    for bit in bits[1:]:
        if bit == current_bit[-1]:
            current_bit += bit
            continue
        bit_array.append(current_bit)
        current_bit = bit
    bit_array.append(current_bit)
    
    min_length = min(len(b) for b in set(bit_array))
    morse_dict = {}
    for b in set(bit_array):
        if len(b) == min_length:
            morse_dict[b] = '.' if '1' in b else ''
        elif len(b) == min_length * 3:
            morse_dict[b] = '-' if '1' in b else ' '
        elif len(b) == min_length * 7:
            morse_dict[b] = '   '
        
    return ''.join(morse_dict[n] for n in bit_array)

def decode_morse(morseCode):
    result = ""
    for word in morseCode.split("   "):
        for ch in word.split(" "):
            result += f"{MORSE_CODE[ch]}"
        result += " "
    return result[:-1]