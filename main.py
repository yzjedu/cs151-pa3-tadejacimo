# Programmers: Theresa DeJacimo
# Course:  CS151, Dr. Zaleem Jembre Yalew
# Due Date: 11/7/24
# PA: 3
# Problem Statement:Displaying a circle, set of lines, or random design
# Data In: type of function and inputs based on the function
# Data Out: design chosen
# Credits: In Class


import random
#Name: set of lines
#Purpose: Output a set of lines using the character, number of characters, and number of lines the user inputs
#Parameters: none
#Return: set of lines with inputted values
def set_of_lines():
    character = str(input('Please enter a character to make your lines with'))
    characters_in_each_line = int(input('Please enter an integer for number of characters in line'))
    number_of_lines = int(input('Please enter an integer for amount of lines you want outputted'))
    one_line = character * characters_in_each_line
    count = 0
    while count < number_of_lines:
        print(one_line)
        count += 1

#Name: circle
#Purpose: Output a circle created by slashes and underscores
#Parameters: none
#Return: circle made from slashes and underscores
def circle():
    print('  _______ \n /       \ \n|         |\n \_______/\n')


#Name: set of lines
#Purpose: Output a set of lines using the character, number of characters, and number of lines the user inputs
#Parameters: none
#Return: random design chosen by computer
def design():
    random_number = random.randint(1, 3)
    print(random_number)
    if random_number == 1:
        # umbrella design from https://www.asciiart.eu/clothing-and-accessories/umbrellas
        print('  .-^-. \n /_/_\_\ \n ` `| ` `\n    j')
    elif random_number == 2:
        #Inpsired by Garfield the fluffy  orange cat
        print('/\_/\_________________/\ ')
        print('| o o |              |\ \ ')
        print('|_{*}_|              | \  \ ')
        print('|                    | \  \ ')
        print('|                    |   \  \ ')
        print('|____________________|    \ /')
        print('    |    |    |     |      *')
        print('    /    |    /     |')
        print('   |^^^^^|   |^^^^^|')
        print('   -------   ------')

    elif random_number == 3:
        count = 0
        while count < 10:
            print(
                '   *****         ******\n *                    *\n  *****           *****\n       *         *\n       *         *')
            count += 1

def main():
    chosen_design = str(input('Please enter "set of lines", "circle" or "random design" to continue.'))
    chosen_design = chosen_design.lower()
    if chosen_design == 'set of lines':
        set_of_lines()
    elif chosen_design == 'circle':
        circle()
    elif chosen_design == 'random design':
        design()
    elif chosen_design == 'stop':
        print('Thank you for using our program, have a nice day!')


main()
