alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

exit = False

print("This is a caesar cipher! Encrypt or Decrypt your message and let it stay a secret!")
print("\n")

def encrypt(text, shift):
    text = text.lower()
    a = list(text)
    shift = int(shift)
    encrypted = ""
    for letter in a:
        x = alphabet.index(letter)
        reqd = (x + shift)%26
        encrypted += alphabet[reqd]

    print(encrypted)

def decrypt(text, shift):
    text = text.lower()
    a = list(text)
    shift = int(shift)
    decrypted = ""
    for letter in a:
        x = alphabet.index(letter)
        reqd = (x - shift)
        decrypted += alphabet[reqd]

    print(decrypted)

while not exit:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if direction == "encode":
            encrypt(text, shift)
        elif direction == "decode":
            decrypt(text, shift)

        go_again = input("Do you want to go again? y or n\n").lower()

        if go_again == "y":
            exit = False
        else: 
            print("Goodbye")
            exit = True
    else:
        print("Invalid choice")
        exit = True

    


    

