import string

# Create a list constant variable of alphanumeric and punctuation string characters using the string module
# Add the " " string to represent a space
ALPHANUMERIC_STRING_LIST = list(string.ascii_lowercase) + list(string.digits) + list(string.punctuation) + [" "]

# Manually create a list of constant variable of Morse code string characters
# Characters which don't translate into Morse code are represented by the "#" character
# Spaces are represented by the "/" character
MORSE_STRING_LIST = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                     "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "-----",
                     ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-.-.--",
                     ".-..-.", "#", "...-..-", "#", ".-...", ".----.", "-.--.", "-.--.-", "#", ".-.-.", "--..--",
                     "-....-", ".-.-.-", "-..-.", "---...", "-.-.-.", "#", "-...-", "#", "..--..", ".--.-.", "#", "#",
                     "#", "#", "..--.-", "#", "#", "#", "#", "#", "/"]

# Create a dictionary consisting of alphabetical keys and Morse code values
alphabet_morse_dict = {ALPHANUMERIC_STRING_LIST[i]: MORSE_STRING_LIST[i] for i in range(len(ALPHANUMERIC_STRING_LIST))}

# Prompt the user to enter the text to be translated to Morse code
text_to_translate = list(input("Enter the text to convert to Morse code: ").lower())

# Perform the translation and amd convert the resulting text string to a list of characters
result_list = [alphabet_morse_dict[i] for i in text_to_translate]

# Convert the translated list of characters to a string and print the result
result = " ".join([str(i) for i in result_list])
print(result)
