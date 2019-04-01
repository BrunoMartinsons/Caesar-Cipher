# I will create an encryption and decryption using the Caesar Cipher
# Caesar Cipher video used to learn: https://www.youtube.com/watch?v=LVHeW1hcdRk

# Encrypting using any number of shifts - Complete :]
# Decrypting using any number of shifts - Complete :]
# Enable user to enter their own alphabet and symbols for use when shifting - Not started
# Turn the encrypt and decrypt into one function (encrypt_and_decrypt) - not started
# User input verification - not started

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def main():
    user_choice = input("Would you like to (encrypt) or (decrypt?) a sentence?")
    if user_choice.lower() == "encrypt":
        shift = int(input("How many shifts do you want? "))
        sentence = input("What sentence do you want to encrypt? ").lower()
        shifted_alphabet = shifting(shift)
        encrypted_word = encrypt(sentence, shifted_alphabet)
        print(encrypted_word)
        input("\nPress enter to close the program")
    elif user_choice.lower() == "decrypt":
        shift = int(input("How many shifts is the encrypted message? "))
        sentence = input("What sentence do you want to decrypt? ").lower()
        shifted_alphabet = shifting(shift)
        decrypted_word = decrypt(sentence, shifted_alphabet)
        print(decrypted_word)
        input("\nPress enter to close the program")
        

def shifting(shift):
    """Shifts the alphabet by the given number"""
    shifted_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for x in range(shift):
        letter_to_shift = shifted_alphabet[0]
        shifted_alphabet.pop(0)  # Removes the first char at index 0.
        shifted_alphabet.insert(25, letter_to_shift)
    return shifted_alphabet


def encrypt(sentence, shifted_alphabet):
    """Encrypts the sentence using the shifted alphabet"""
    encrypted_word = []

    for char in sentence:
        char_exist = False  # Is char in the alphabet?
        for letter in alphabet:
            if char == letter:
                char_exist = True
                index = alphabet.index(letter)
                encrypted_word.append(shifted_alphabet[index])
            else:
                # If letter is last in alphabet and char from sentence not in alphabet append the char.
                if alphabet.index(letter) == 25 and char_exist == False:
                    encrypted_word.append(char)

    encrypted_word = "".join(encrypted_word)
    return encrypted_word


def decrypt(sentence, shifted_alphabet):
    """Decrypts the sentence using the shifted alphabet"""
    decrypted_word = []

    for char in sentence:
        char_exist = False  # Is char in the shifted_alphabet?
        for letter in shifted_alphabet:
            if char == letter:
                char_exist = True
                index = shifted_alphabet.index(letter)
                decrypted_word.append(alphabet[index])
            else:
                # If letter is last in shifted_alphabet and char from sentence not in shifted_alphabet append the char.
                if shifted_alphabet.index(letter) == 25 and char_exist == False:
                    decrypted_word.append(char)

    decrypted_word = "".join(decrypted_word)
    return decrypted_word


#main()

"""-----------------------------------------------------------"""
# The above method is the long way to do it
# Now I will use the ord() and chr() methods (ascii).
# ord("A") = 65, chr(65) = "A"

def simple_main():
    user_choice = input("Would you like to (encrypt) or (decrypt?) a sentence?")
    if user_choice.lower() == "encrypt":
        shift = int(input("How many shifts do you want? "))
        sentence = input("What sentence do you want to encrypt? ")
        encrypted_sentence = simple_encrypt(sentence, shift)
        print(encrypted_sentence)
        input("\nPress enter to close the program")
    elif user_choice.lower() == "decrypt":
        shift = int(input("How many shifts is the encrypted message? "))
        sentence = input("What sentence do you want to decrypt? ")
        decrypted_sentence = simple_decrypt(sentence, shift)
        print(decrypted_sentence)
        input("\nPress enter to close the program")
        

def simple_encrypt(sentence, shift):
    """Encrypts the sentence using the shift"""
    encrypted_sentence = ""
    for char in sentence:
        if char.isalpha() == False:  # If char is not a letter
            encrypted_sentence += char
        elif char.isupper() == True and (ord(char) + shift) > ord("Z"):
            total_number = ord(char) + shift
            while total_number > ord("Z"):
                total_number -= 26
            encrypted_sentence += chr(total_number)
        elif char.islower() == True and (ord(char) + shift) > ord("z"):
            total_number = ord(char) + shift
            while total_number > ord("z"):
                total_number -= 26
            encrypted_sentence += chr(total_number)
        else:
            encrypted_sentence += chr((ord(char) + shift))
    return encrypted_sentence


def simple_decrypt(sentence, shift):
    """Decrypts the sentence using the shift"""
    decrypted_sentence = ""
    return decrypted_sentence

simple_main()

