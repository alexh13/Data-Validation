breakBetweenExamples = '--------------- break between examples ---------------'

# Basic validation telling the user if their input is acceptable
# or not


def isValidEmailCharacter(character):
    # character must be alphanumeric or an underscore, hyphen, or period.
    # The \ at the end of each line lets me continue one long line of
    #     code across multiple lines of text.
    return (('A' <= character <= 'Z') or
            ('a' <= character <= 'z') or
            ('0' <= character <= '9') or
            (character in '_-.'))


print(breakBetweenExamples)


def isValidEmail(email):
    if type(email) != str:     # email address must be a string
        return False
    if email.count('@') != 1:  # email must contain exactly one @ symbol
        return False
    parts = email.split('@')   # split the email into the first part and the second part
    for character in parts[0]: # check the characters in the first half of the email address
        if not isValidEmailCharacter(character):
            return False
    for character in parts[1]: # check the characters in the second half of the email address
        if not isValidEmailCharacter(character):
            return False
    if '..' in parts[1]:
        # second part can't contain two periods in a row
        return False
    if not '.' in parts[1]:
        # second part must have at least one period
        return False
    if parts[1][0] == '.' or parts[1][-1] == '.':
        # second part can't begin or end with a period
        return False
    # since address did not fail any of the checks above, it must be valid
    return True


print(breakBetweenExamples)


def getEmail():
    #
    # Version 1 - ask for input, then loop if input is invalid
    #
    result = input('Enter your email address:')         # initial request for user input
    while not isValidEmail(result):                     # checks whether input is valid
        print('The address you entered is not valid.')  # communicate clearly with user
        result = input('Enter a valid email address:')  # ask again for input
    return result                                       # result is guaranteed to be valid
    #
    # Version 2 - start with an infinite loop and break out if valid
    #
    while True:
        result = input('Enter your email address:')     # request for user input
        if isValidEmail(result):                        # checks whether input is valid
            break                                       # break out of the loop if email address is valid
        print('The address you entered is not valid.')  # communicate clearly with user
    return result
    #
    # Version 3 - start with an infinite loop and continue if invalid
    #
    while True:
        result = input('Enter your email address:')         # request for user input
        if not isValidEmail(result):                        # checks whether input is valid
            print('The address you entered is not valid.')  # communicate clearly with user
            continue                                        # continue at the top of the next iteration
        break                                               # break out of the loop if email address is valid
    return result


print(breakBetweenExamples)


# ------------------------------------------
# ------------------------------------------

# Asks the user for an integer until I can
# successfully convert what the user types into an integer.

def getInt():
    try:
        # If result of input() can successfully be interpreted as an integer this line will succeed.
        return int(input('Enter an integer:'))
    except:
        # If anything goes wrong, an exception will be thrown.
        # Notifies user, then loops again.
        print('Invalid input. Try again.')
