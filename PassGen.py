# Author      : varnull
# Version     : v1.0.0
# Description : A simple alphanumeric password generator

import string
import random
import sys
import os  # Allows access to the operating system
import termcolor as tc  # Colours the text of print statements

# PROMPTS & OUTPUT STRINGS
title = """
_________________________________________________________________________________________
   ___                                    _   ___                          _             
  / _ \__ _ ___ _____      _____  _ __ __| | / _ \___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 / /_)/ _` / __/ __\ \ /\ / / _ \| '__/ _` |/ /_\/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
/ ___/ (_| \__ \__ \\\ V  V / (_) | | | (_| / /_\\\  __/ | | |  __/ | | (_| | || (_) | |   
\/    \__,_|___/___/ \_/\_/ \___/|_|  \__,_\____/\___|_| |_|\___|_|  \__,_|\__\___/|_|
_________________________________________________________________________________________
                                  """ + tc.colored("Type Ctrl-C to exit.", "red")
                                  
copied_to_clipboard = tc.colored("    Copied to clipboard.", "magenta")
invalid_number_input = tc.colored("\n⚠️   Invalid Input - please enter a valid number. ⚠️  ", "white", "on_red")
invalid_yn_input = tc.colored("\n⚠️   Invalid Input - please enter either 'Y' or 'N'. ⚠️  ", "white", "on_red")
goodbye = tc.colored("\n👋 Goodbye.\n", "white", "on_red")

 # Copies a given string to the users clipboard
def copy_to_clipboard(x):
    command = "echo " + x.strip() + " | clip"
    os.system(command)
    print(copied_to_clipboard)


# Generates a random alphanumeric password containing uppercase, lowercase, numeric and symbolic characters at a given length
def generate_password(length):
    charset = list(string.ascii_uppercase + string.ascii_lowercase + "0123456789" + "!£$€%^*@;~#")
    indexes = [random.randrange(0, len(charset)) for i in range(length)]
    return "".join(charset[i] for i in indexes)


# Creates a yes/no [Y/n] prompt at the terminal with a given prompt text
def yes_no_prompt(text):

    while True:
        choice = str(input(text + " " + tc.colored("[Y/n]", "blue") + ": ")).upper()
        if choice == "Y":
            return True
        elif choice == "N":
            return False
        else: 
            print(invalid_yn_input)


# Version of the program to generate a password when given a length argument at the terminal
def argument_mode():

    try:
        length = int(sys.argv[2])
        if length > 0 and length < 100:
            password = generate_password(length)
            print(tc.colored("\n🔑  Generated password: ", "yellow") + password)
            copy_to_clipboard(password)
        else:
            print(invalid_number_input)
    except ValueError:
        print(invalid_number_input)
    except IndexError:
        print("\n" + tc.colored("[PasswordGenerator] Please enter an argument, use '-h' for more information.", "white", "on_red") + "\n")

    
def print_help_message():
    
    t = tc.colored("                      🔑 PasswordGenerator                      ", "white", "on_magenta")
    print("\n" + t + 
"""

Generates random alphanumeric passwords given a specific length.

OPTIONS:

-m    Launches the menu mode
-l    Specifies a length and uses argument mode
-h    Shows this help menu

""")


# Version of the program with a full interactive looped menu
def menu_mode():

    while True: # Main menu loop
        
        os.system("cls")
        print(tc.colored(title, "blue"))

        while True: # Entering password length w/ type mismatch exception handelling
            try:
                length = int(input(tc.colored("\n📏  Enter password length: ", "cyan")))
                if length > 0 and length < 100: break
                else:
                    print(invalid_number_input)
                    continue
            except ValueError:
                print(invalid_number_input)

        password = ""
        password = generate_password(length)

        print("\n🔑  " + tc.colored("Generated password", "yellow") + ": " + tc.colored(password, "white", "on_magenta"))

        if yes_no_prompt(tc.colored("\n⌨️   Copy to clipboard?", "cyan")):
            copy_to_clipboard(password)

        if yes_no_prompt(tc.colored("\n🔁  Generate another?", "cyan")):
            os.system("cls")
            continue
        else:
            print(goodbye)
            exit()


def main(): # Main function 
    if len(sys.argv) > 1:
        if sys.argv[1] == "-l":
            argument_mode() # If an argument for length is provided at the command line, switch to argument mode.
        elif sys.argv[1] == "-m":
            try: menu_mode()
            except KeyboardInterrupt:
                print(goodbye)
                exit()    
        elif sys.argv[1] == "-h":
            print_help_message()
        else:
            print("\n" + tc.colored("[PasswordGenerator] Invalid option - Use 'h' for more information.", "white", "on_red") + "\n")
    else:
        print_help_message()
        


if __name__ == '__main__':
    main()
