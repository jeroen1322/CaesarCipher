import time
import codecs

print()
string_input = input("Please enter a sentence to encode or decode:\n")

encode = codecs.getencoder("rot-13")
result = encode(string_input)[0]
print("\nProcessing.....")
time.sleep(0.5)
print("\nMessage:")
print(result)

input("\n\n")
