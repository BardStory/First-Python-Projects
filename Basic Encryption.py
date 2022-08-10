#Author Joshua Bard

message = str(input("Enter your first name"))
key = str(input("Please insert a key"))
alphabet = 26

print("First name: " + message)
print("Key: " + key)

def viginere_encrypt(message, key):
    length = len(message)
    mnum = [0]*length
    
    for i in range(0, length):
        mnum[i] = letter_to_number(message[i])
    knum = [0]*len(key)
    
    for i in range(0, len(key)):
        knum[i] = letter_to_number(key[i])
        result = [0]*length
        
    for i in range(0, length):
        result[i] = number_to_letter(mnum[i] + knum[i % len(key)])
    
    return result

def letter_to_number(letter):
    return ord(letter) - ord("a")

def number_to_letter(number):
    return chr(number%alphabet + ord("a"))

answer = viginere_encrypt(message, key)
str1 = ''.join(answer)
print("Encrypted text: " + str(str1))