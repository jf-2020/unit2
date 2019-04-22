# cipher_exercises.py - this prgm will implement the problem from 4/22 AM's
#                       discussion. namely, the user will attempt to guess
#                       the stored password. the password itself will be encoded
#                       via a simple ceasar cipher (i.e. ROT13). the user will
#                       be allowed to dynamically interact, receiving feedback
#                       as to which characters are correct in their respective
#                       guess.
#
# jf - 4/22


##############################################################################
# first, we must create a function to encode a given plaintext string into an
# encoded string via a ceasar cipher. n.b. this is a rotate 13 cipher.
##############################################################################


def encode(plaintext):
    '''
    parameter:
        plaintext   -> String
    return:
        ciphertext  -> String
    '''

    # n.b. this only works with lowercase letters

    # we will do this via a simple dictionary mapping
    translate_dict = {
                      'a' : 'n',
                      'b' : 'o',
                      'c' : 'p',
                      'd' : 'q',
                      'e' : 'r',
                      'f' : 's',
                      'g' : 't',
                      'h' : 'u',
                      'i' : 'v',
                      'j' : 'w',
                      'k' : 'x',
                      'l' : 'y',
                      'm' : 'z',
                      'n' : 'a',
                      'o' : 'b',
                      'p' : 'c',
                      'q' : 'd',
                      'r' : 'e',
                      's' : 'f',
                      't' : 'g',
                      'u' : 'h',
                      'v' : 'i',
                      'w' : 'j',
                      'x' : 'k',
                      'y' : 'l',
                      'z' : 'm'    
                     } 

    # init a return string that'll be concatenated to as
    # the ciphertext is generated
    ciphertext = ''

    # first, we'll loop over the passed plaintext
    for char in plaintext:

        # then we'll perform a lookup in the translate dictionary
        ciphered_character = translate_dict[char]

        # and finally concatenate it to the ciphertext string
        ciphertext += ciphered_character

    return ciphertext


def test_encode():
    # test function for the testing 'encode()'

    test = 'abc'
    correct_test_value = 'nop'
    encoded = encode(test)

    print("Testing encode('" + test + "')...")
    print("Correct ciphertext: " + correct_test_value)
    print("Tested ciphertext: " + encoded + " => " + str((encoded == correct_test_value)))


######################################################################################
# Second, we need to create a function that will allow the user to input a test string
# against which the hashed password will be checked. moreover, it'll allow the user to
# dynamically check the individually hashed characters. that is to say, it'll let the
# user know which characters in their guess are correct.
######################################################################################


def guess_and_check(test_password, real_password):
    '''
    parameters:
        test_password -> String
        real_password -> String
    return:
        correct         -> Boolean
        correct_indices -> List
    '''

    ########################
    # init our return values
    ########################

    # is the guess correct?
    correct = False

    # what about the indices? which ones are correct?
    correct_indices = [False for _ in range(len(real_password))]

    ########################
    ########################

    # go ahead and return if the lengths aren't correct
    if len(test_password) != len(real_password):
        return correct, correct_indices

    # iterate through the test password & keep track of the index
    for index, char in enumerate(test_password):

        # get it's ceaser ciphered value
        encoded_character = encode(char)

        # then check whether or not it matches the cipher text @ that particular index
        if encoded_character == real_password[index]:

            # if it is, update that it's true within the correct_indices return value
            correct_indices[index] = True

    # finally, if all the indices are correct, return correct as true
    if correct_indices == [True for _ in range(len(real_password))]:
    
        # update correct to reflect that fact
        correct = True

        # and return it
        return correct, correct_indices

    else:

        # otherwise, it's not the correct guess
        return correct, correct_indices

    
def test_guess_and_check():
    # test function for guess_and_check()

    test_password = 'abc'
    real_password = 'nop'

    print("Testing guess_and_check('" + test_password + ", '" + real_password + "')")
    
    # is the guess the correct hashed value?
    guess_and_check_return_value = guess_and_check(test_password, real_password)
    print("Correct: (True/False)? " + str(guess_and_check_return_value[0]))

    # what about the case where the length of guess is not the same as the real password's
    # length?

    real_password_shorter = 'no'
    real_password_longer = 'nopl'

    # is the guess the correct hashed value for the shorter password?
    guess_and_check_return_value_shorter = guess_and_check(test_password, real_password_shorter)
    print("Correct: (True/False)? " + str(guess_and_check_return_value_shorter[0]))

    # is the guess the correct hashed value for the longer password?
    guess_and_check_return_value_longer = guess_and_check(test_password, real_password_longer)
    print("Correct: (True/False)? " + str(guess_and_check_return_value_longer[0]))


def main():
    # main method for the entire problem. runs all necessary functions

    # init a real password
    real_password = 'nop'

    # ask user whether or not they want to play the password guessing game
    play_the_game = input("Do you want to play the password guessing game? (y/n) ")

    # play?
    if play_the_game == 'y':

        # first, we need to allow the user to guess a password
        password_guess = input("Guess the password (a string of lowercase characters ONLY): ")

        # second, we need to tell the user whether or not it's the correct length if necessary
        while len(password_guess) != len(real_password):
            print("The real password and the given password don't have the same length! Try %d characters instead" % len(real_password))

            # let them update their password guess
            password_guess = input("Guess the password (a string of lowercase characters ONLY): ")

        # third, we begin to perform the password checking
        guess_correct = guess_and_check(password_guess, real_password)[0]
        guess_indices = guess_and_check(password_guess, real_password)[1]

        # if it's not correct, then we must let the user continue guessing
        while not guess_correct:

            # let them know what indices aren't correct
            for index, value in enumerate(guess_indices):

                if value == False:
                    print("The character at index %d is incorrect. Try another character for that place." % index)

            # update their guess
            new_password_guess = input("Try guessing the password (a string of lowercase characters ONLY) again: ")

            # check that guess
            guess_correct = guess_and_check(new_password_guess, real_password)[0]

            # get the new guess indices
            guess_indices = guess_and_check(new_password_guess, real_password)[1]

        # if this point of execution is reached, then you've guessed the password correctly!
        print("Congratulations, you've guessed the password correctly!")

    # no play...
    else:

        print("Okay. Fair enough. Quitting...")


# to be run as script
if __name__ == "__main__":

    # test the ceasar cipher function
    # test_encode()
    ### works ###

    # test the guess and check function
    # test_guess_and_check()
    ### works ###

    main()