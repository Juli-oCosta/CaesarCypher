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

alphabet = list(map(chr, range(97, 123)))

def caesarCypher(original_text, shift_amount, encode_or_decode):
    rearranged_text = []

    if encode_or_decode == "decode":
      shift_amount *= -1 # Invert to decode

    for letter in original_text:
      if letter not in alphabet:
        rearranged_text.append(letter)
      else:
        position = alphabet.index(letter)
        new_position = (position + shift_amount) % 26 # Prevents it from being left out of index
        new_letter = alphabet[new_position]

        rearranged_text.append(new_letter)

    print(f"Here's the {encode_or_decode}d result:", *rearranged_text)

over = False
while not over:
  while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode" or direction == "decode":
      break
    else:
      print("Invalid option. Please, type only 'encode' or 'decode'.")

  text = input("Type in your message:\n").lower()

  while True:
    try:
      shift = int(input("Type the shift number:\n"))
      break
    except ValueError:
      print("Invalid option. Please, type only an integer number.")

  caesarCypher(original_text=text, shift_amount = shift, encode_or_decode=direction)

  while True:
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
      over = True
      print("Goodbye!")
      break
    elif restart == "yes":
      break
    else:
      print("Invalid option. Please, type only 'yes' or 'no'.")
