import string
import time

int_list = []
char_list = []
message = []
alphabet = string.ascii_lowercase

while True:
    try:
        key = int(input("Key: "))
        if(key > 13) | (key < 1):
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
    print("{} + {} = {} = {}".format(number, key, calc, alphabet[calc]))
    char_list.append(calc)

for i in char_list:
    if(i > 25):
        i = i - 26
        print("Making some corrections.... {} - 26 = {} = {}".format(i, i-26, alphabet[i]))
    elif(i < 0):
        i = i + 26
        print("Making some corrections.... {} + 26 = {} = {}".format(i, i+26, alphabet[i]))

    message.append(alphabet[i])

print("\n #### MESSAGE #### \n")
for i in message:
    print(i, end='')

input("\n\n")
