import string

int_list = []
char_list = []
alphabet = string.ascii_lowercase

while True:
    try:
        key = int(input("Key: "))
    except ValueError:
        print("Sorry, that is not a valid key.\n")
    else:
        break

string_input = input("Please enter a sentence: \n\n")
string_list = list(string_input)

b = int(0)

for character in string_input:
    number = ord(character) - 97
    int_list.append(number)
    calc = number + key
    print("Calculating.... \n")
    print("{} + {} = {}".format(number, key, calc))
    char_list.append(calc)

for i in char_list:
    if(i > 25):
        print("{} - 26 = {}".format(i, i-26))
        i = i - 26
    elif(i < 0):
        print("{} + 26 = {}".format(i, i+26))
        i = i + 26

    print(alphabet[i], end='')



