BEEP = "Beep"
BOOP = "Boop"
GOOD_VOLTAGE = 1.2
is_entering = True
sound_list = []
INVALID = "Not robot compliant!!"

while is_entering:
    try:
        voltage = float(input("Enter your input: "))
        
    # Catches all non-numeric inputs
    except:
        print(INVALID)
        
    else:
    
        # Checks if voltage is negative and breaks loop.
        if voltage < 0:
            break
    
        # Checks if voltage is good
        elif voltage >= GOOD_VOLTAGE:
            sound_list.append(BEEP)
        
        else:
            sound_list.append(BOOP)
        

# Prints Beeps and boops one line after the other
for sound in sound_list:
    print(sound)