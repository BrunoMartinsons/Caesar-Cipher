# I will create an encryption and decryption using the Caesar Cipher
# Caesar Cipher video used to learn: https://www.youtube.com/watch?v=LVHeW1hcdRk

# Encrypting using any number of shifts - Complete :]
# Decrypting using any number of shifts - Not started
# Enable user to enter their own alphabet and symbols for use when shifting - Not started

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def main():
    shift = int(input("How many shifts do you want? "))
    sentence = input("What sentence do you want to encrypt? ").lower()
    shifted_alphabet = shifting(shift)
    encrypted_word = encrypt(sentence, shifted_alphabet)
    print(encrypted_word)


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


main()