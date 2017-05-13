# Import the dependencies
import string
import time

# Declare some stuff
int_list = []
char_list = []
message = []
alphabet = string.ascii_lowercase
result = ""

# Make sure the user input for the key is an integer
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

# Get the user's string that the user wants to encode
string_input = raw_input("\nPlease enter a sentence (WITHOUT SPACES):\n")

# Act like the system is working hard
print("\nProcessing.....\n")
time.sleep(1)

# Do the actual encoding
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

# Append the letters to the result string
print("\n #### MESSAGE #### \n")
for i in message:
    result += i

# Print the encoded result
print(result)
