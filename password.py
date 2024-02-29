#import string and random module
import string
import random
#define characters that can be used in password
all_characters=string.ascii_letters+string.digits+string.punctuation
print("Welcome to password generator\n")
#ask the user for length of password
length=int(input("Enter the length of password:"))
#generate password using randomly choosen characters
#using the 'choices'function from random module join resulted characters into string
password=''.join(random.choices(all_characters,k=length))
#display generated password to user
print("Generated password is:",password)