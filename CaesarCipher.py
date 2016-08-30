import string
import time

int_list = []
char_list = []
message = []
alphabet = string.ascii_lowercase

while True:
    try:
        key = int(input("Key (Between 1 and 26): "))
        if(key > 26) | (key < 1):
            print("The key should be between 1 and 13 \n")
            continue
    except ValueError:
        print("Sorry, that is not a valid key.\n")
    else:
        break

string_input = input("Please enter a sentence: (WITHOUT SPACES) \n\n")

print("Processing.....\n")
time.sleep(1)
string_input = string_input.lower()
for character in string_input:
    number = ord(character) - 97
    int_list.append(number)
    calc = number + key
    char_list.append(calc)

for i in char_list:
    if(i > 25):
        i = i - 26
    elif(i < 0):
        i = i + 26

    message.append(alphabet[i])

print("\n #### MESSAGE #### \n")
for i in message:
    print(i, end='')

input("\n\n")
