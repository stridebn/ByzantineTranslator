import mappings
import rip_unicode
import helpers
from music21 import *

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
            if special == "ROK":
                symbol_list.append("Oligon with Kentemata (combined)")
                movement_list.append(helpers.OLIGON)
                movement_list.append(helpers.KENTEMATA)
            elif special == "R2A":
                symbol_list.append(movement[-1])
                movement_list.append(helpers.APOSTROPHOS)
                movement_list.append(helpers.APOSTROPHOS)
            elif special == "RE":
                symbol_list.append(movement[-1])
                movement_list.append(helpers.ELAPHRON)
            else:
                symbol_list.append(movement[-1])
                movement_list.append(movement[:-1])
        elif char in accidental:
            duration_change, dur_forward, dur_back = accidental[char]
            for i in range(dur_back):
                item=0-1-i
                movement_list[item][4] = duration_change
        else:
            symbol_list.append("Unknown Symbol")
            movement_list.append("")

    return symbol_list, movement_list

def generate_melody(movements, starting_pitch):
    melody = stream.Stream()
    melody.clear()
    melody.append(meter.TimeSignature())
    print(f"Starting pitch: {starting_pitch}")
    current_pitch = pitch.Pitch(starting_pitch)
    current_note = note.Note()
    current_note.pitch = current_pitch
    scale_degrees = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    print(len(movements))
    for element in movements:
        if (len(element) > 2):
            direction, magnitude, stress = element[:3]
            # duration = element[3]
            print(f"Reading {element[:3]}")
            current_degree_index = scale_degrees.index(current_pitch.step)
            print(f"Current index: {current_degree_index}")
            print(f"Note before change: {current_note.pitch}")
            # Apply stress
            # if stress == 'S':
            #     current_note.articulations.append(articulations.Accent)
            # elif stress == 'U':
            #     # Unstressed - example, could add more nuance here
            #     current_note.articulations.append(articulations.Tenuto)

            # Calculate next note based on direction and magnitude
            if direction == 'U':
                next_degree_index = (current_degree_index + magnitude) % len(scale_degrees)
            elif direction == 'D':
                next_degree_index = (current_degree_index - magnitude) % len(scale_degrees)
            else:
                next_degree_index = current_degree_index  # No change
        
            next_pitch_step = scale_degrees[next_degree_index]
            current_pitch = pitch.Pitch(next_pitch_step + str(current_pitch.octave))
            
            # Adjust octave if necessary (this is a simplified logic)
            if direction == 'U' and next_degree_index < current_degree_index:
                current_pitch.octave += 1
            elif direction == 'D' and next_degree_index > current_degree_index:
                current_pitch.octave -= 1
            current_note.pitch = current_pitch
            melody.append(current_note)
            print(f"The note after is : {current_note.pitch}\n~~~")
            current_note = note.Note()
            # current_note.pitch.midi = melody[-1].pitch.midi + interval
            # Adjust current note pitch
    for ts in melody.recurse().getElementsByClass(meter.TimeSignature):
        melody.remove(ts)
    return melody

def generate_melody_lilypond(movements, starting_pitch):
    # Initialize the LilyPond notation with the starting pitch
    # Assuming starting_pitch is in LilyPond format (e.g., "c' for middle C)
    lilypond_notation = "\\relative " + starting_pitch + " {\n"
    
    # Calculate the current pitch in MIDI to manage intervals
    # This is a simplification. You might need a more complex logic for real applications.
    current_midi_pitch = note.Note(starting_pitch).pitch.midi
    
    for element in movements:
        if len(element) < 3:  # Adjusted to 3 since stress can be ''
            break
        
        direction, magnitude, stress = element[:3]
        
        # Convert direction and magnitude to LilyPond pitch notation
        if direction == 'U':
            lilypond_pitch = "'" * magnitude  # Upward movement in LilyPond
        elif direction == 'D':
            lilypond_pitch = "," * magnitude  # Downward movement in LilyPond
        else:
            lilypond_pitch = ""  # No movement, stay on the same pitch
        
        # Apply stress (articulation) if any
        if stress == 'S':
            articulation = "-> "  # Staccato for demonstration, choose as per your requirement
        elif stress == 'U':
            articulation = "-- "  # Tenuto, or choose another symbol as needed
        else:
            articulation = ""  # No articulation
        
        # Append the note to the LilyPond notation
        lilypond_notation += articulation + lilypond_pitch + " "
        
        # Here, we simulate changing the MIDI pitch based on direction and magnitude
        # This is a placeholder logic; for actual note calculation, use music theory rules
        if direction == 'U':
            current_midi_pitch += magnitude
        elif direction == 'D':
            current_midi_pitch -= magnitude
    
    lilypond_notation += "\n}"
    
    return lilypond_notation

# Example usage:
pdf_path = 'TrainingData/b5109.pdf'
charlist = rip_unicode.extract_special_unicode_chars(pdf_path)  # List of Unicode characters to decode
starting_pitch = 'C4'
starting_pitchly = "c'"
# if helpers.is_sublist(charlist, helpers.TONE8):
#     starting_pitch = 'G4'
#     starting_pitchly = 'g4'
# if helpers.is_sublist(charlist, helpers.TONE3):
#     starting_pitch = 'F4'
#     starting_pitchly = 'f4'
starting_pitch = helpers.get_tone(charlist)[0]
symbols, movements = decode_unicode(charlist)
for ele in movements:
    print(ele)
melody = generate_melody(movements, starting_pitch)
melody.show('musicxml')
# melody = generate_melody(movements, starting_pitch)
# print("Symbols:", symbols)
# print("Movements:", movements)