import mappings

def decode_unicode(charlist):
    symbol_list = []
    movement_list = []

    # Associate symbol and movements in the following format:
    # pitch direction | U=Up, D=Down, -=No Movement
    # pitch magnitude | (1-7), indicating the number of steps on the scale to move
    # ornaments | S=Stressed, U=Unstressed
    # duration | Represented as either a whole number (for multiple beats) OR a decimal point and then a partial value (.5 (gorgon), .3 (digorgon), .25 (trigorgon))

    # Example mapping based on hypothetical symbols and descriptions
    # symbol_to_movement = {
    #     '\uf063': ('', '', '', 0, 'Ison'),  # Stay same
    #     '\uf078': ('U', '1', 'U', 0, 'Kentemata'), # Up one unstressed
    #     '\uf073': ('U', '1', '', 0, 'Oligon'), # Up one
    #     '\uf053': ('U', '1', 'S', 0, 'Petaste'), # Up one stressed
    #     '\uf06A': ('D', '1', '', 0, 'Apostrophos')  # Down one step
    # }
    accidental = {
        '\uf02A': (2, 0, 0)
    }

    # Interpret each character in the input list
    
    duration_change = None
    dur_forward = 0
    for char in charlist:
        if char in mappings.my_map:
            direction, magnitude, stress, special, name = mappings.my_map[char]
            movement = [direction,magnitude,stress,special,name]
            if (dur_forward > 0) :
                dur_forward -=1 
                movement[-1] = duration_change
                # symbol_list[-1] = name
                # movement_list[-1] = name
            symbol_list.append(movement)
        elif char in accidental:
            duration_change, dur_forward, dur_back = accidental[char]
            for i in range(dur_back):
                item=0-1-i
                movement_list[item][4] = duration_change
        else:
            symbol_list.append("Unknown Symbol")
            movement_list.append("")

    return symbol_list, movement_list

# Example usage:
charlist = ['\uf021', '\uf033']  # List of Unicode characters to decode
symbols, movements = decode_unicode(charlist)
print("Symbols:", symbols)
print("Movements:", movements)