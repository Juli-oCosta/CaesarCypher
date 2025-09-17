logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88
              88
              88
"""

print(logo)

# Creates an alphabet list from 'a' to 'z' that serves as a map for the cipher
alphabet = list(map(chr, range(97, 123)))

def caesarCypher(original_text, shift_amount, encode_or_decode):
  # Initializes an empty list to store the resulting text.
    rearranged_text = []

    # For decryption, simpli invert the siign of the shift amount
    if encode_or_decode == "decode":
      shift_amount *= -1

    # Iterates over each character in the original text
    for letter in original_text:
      if letter not in alphabet:
        # If it's not a letter (e.g., space, number, symbol), keep the original character
        rearranged_text.append(letter)
      else:
        # If it is a letter, apply the cipher logic
        # Finds the current position of the letter in the alphabet (0-25)
        position = alphabet.index(letter)

        # Calculates the new position, using the modulus operator (%) to ensure the wrap-around
        # (making the alphabet work like a circle)        
        new_position = (position + shift_amount) % 26

        # Gets the new letter based on the calculated new position
        new_letter = alphabet[new_position]
        rearranged_text.append(new_letter)

    print(f"Here's the {encode_or_decode}d result:", *rearranged_text)

# --- Main Program Logic ---

# Flag to control the execution of the main loop
over = False
while not over:

  # --- Direction Validation ---
  # Validation loop to ensure the user enters a valid direction
  while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode" or direction == "decode":
      break # If the input is valid, break out of this validation loop
    else:
      print("Invalid option. Please, type only 'encode' or 'decode'.")

  text = input("Type in your message:\n").lower()

  # --- Shift Validation ---
  # Validation loop to ensure the user enters an integer for the shift
  while True:
    try:
      shift = int(input("Type the shift number:\n"))
      break
    except ValueError:
      print("Invalid option. Please, type only an integer number.")

  caesarCypher(original_text=text, shift_amount = shift, encode_or_decode=direction)

  # --- Restart Option Validation ---
  # Loop to ensure the user chooses 'yes' or 'no'
  while True:
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
      over = True # Updates the flag to end the main program loop.
      print("Goodbye!")
      break
    elif restart == "yes":
      break
    else:
      print("Invalid option. Please, type only 'yes' or 'no'.")
