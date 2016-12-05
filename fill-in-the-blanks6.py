# IPND Stage 2 Final Project
import sys

# Easy start phrase - taken from starter code
current_phrase_list = ["A common first thing to do in a language is display \
    'Hello ___1___!'  In ___2___ this is particularly easy; all you have to \
    do is type in: ___3___ 'Hello ___1___!' \
\
    Of course, that isn't a very useful thing to do. However, it is an \
    example of how to output to the user using the ___3___ command, and \
    produces a program which does something, so it is useful in that \
    capacity.\
\
    It may seem a bit odd to do something in a Turing complete language that \
    can be done even more easily with an ___4___ file in a browser, but it's \
    a step in learning ___2___ syntax, and that's really its purpose.",
# Medium start phrase - taken from starter code
    "A ___1___ is created with the def keyword. You specify the inputs\
    a ___1___ takes by adding ___2___ separated by commas between the \
    parentheses.\
\
    ___1___s by default return ___3___ if you don't specify the value to \
    return.___2___ can be standard data types such as string, number, \
    dictionary, tuple,and ___4___ or can be more complicated such as \
    objects and lambda functions.",\
# Hard start phrase - taken from Monty Python
    "We're knights of the round ___1___. We dance when e're we're \
    ___2___. We do routines, and chorus-scenes, with footwork ___3___. We \
    dine well here in ___4___. We eat ___5___, and ___6___, and ___7___ a \
    lot.\
\
    We're knights of the round ___1___. Our shows are ___8___. But many \
    times,we're given rhymes, that are quite ___9___. We're opera mad in \
    ___4___. We sing from the ___10___ a lot."]

blank_number = 1  # guessing blank number
answers_list = [["world", "python", "print", "html"],
                ["function", "arguments", "none", "list"],
                ["table", "able", "impeccable", "camelot", "ham", "jam",
                "spam", "formidable", "unsingable", "diaphragm"]]


def word_in_pos(word, word_list):
    """Take in a string (word) and a list of strings (word_list)and check
    (word) against (word list) and if theres match, return the matching
    string. If no match, return None"""
    for string in word_list:
        if string in word:
            return string
    return None


def correct(num, guess):
    """Takes in a number (num), and a second string (guess),
    and replace all (num) blanks in(current_phrase) with (guess)
    Return an updated string (current_phrase)"""
    global current_phrase
    rep = []  # replacement list
    blank = "___" + str(num) + "___"
    for word in current_phrase.split(' '):
        replacement = word_in_pos(guess, answers)
        if replacement is not None:
            word = word.replace(blank, guess)
            rep.append(word)
        else:
            rep.append(word)
        current_phrase = ' '.join(rep)
    return current_phrase


def difficulty(a):
    """Take in string (a) which must be easy medium or hard
    Return selected difficulty's (current_phrase) from (current_phrase_list)
    and selected difficulty's (answers) from (answers_list)"""
    global current_phrase
    global answers
    if a == "easy":
        answers = answers_list[0]
        current_phrase = str(current_phrase_list[0])
        return current_phrase, answers
    elif a == "medium":
        answers = answers_list[1]
        current_phrase = str(current_phrase_list[1])
        return current_phrase, answers
    elif a == "hard":
        answers = answers_list[2]
        current_phrase = str(current_phrase_list[2])
        return current_phrase, answers
    else:
        print "INVALID SELECTION! YOU LOSE! GOOD DAY, SIR!"
        sys.exit()


def is_number(s):
    """Takes in string (s) and return True if number, False if not
    Found here - http://stackoverflow.com/questions/354038/how-do-
    i-check-if-a-string-is-a-number-float-in-python"""
    try:
        float(s)
        return True
    except ValueError:
        return False


""" START OF GAME - Difficulty selection"""
diff_input = raw_input("Choose a difficulty: easy, medium, or hard.\
    Incorrect input will result in a loss.").lower()
difficulty(diff_input)

guesses_left = (raw_input("Choose the number of guesses before you \
    lose."))
while is_number(guesses_left) == False:
    print "Try a number this time. "
    guesses_left = (raw_input("Choose the number of guesses before you \
    lose."))
guesses_left = int(guesses_left)
if guesses_left <= 0:
    print "YOU LOSE! GOOD DAY, SIR!"
    sys.exit()

print "You have chosen: " + diff_input
print " "
print "You will get " + str(guesses_left) + " guesses per problem."
print " "
print "Current phrase:"
print current_phrase

# First guess
current_guess = raw_input("What word should fill in the blank(s) for " +
    "___" + str(blank_number) + "___" + "? :").lower()

# Start of standard game loop
while guesses_left > 0 and blank_number < len(answers):
    if current_guess == answers[blank_number-1]:  # Correct input
        print "Correct answer!"
        print " "
        correct(blank_number, current_guess)
        print "Current phrase:"
        print current_phrase
        blank_number += 1
        current_guess = raw_input("What word should fill in the blank(s) \
            for " + "___" + str(blank_number) + "___" + "? :").lower()
    else:  # Incorrect input
        guesses_left -= 1
        if guesses_left == 1:
            print "Wrong answer, try again. Guesses left: " + \
            str(guesses_left) + " Make it count!"
            current_guess = raw_input("What word should fill in the blank(s) \
                for " + "___" + str(blank_number) + "___" + "? :").lower()
        elif guesses_left > 0:
            print "Wrong answer, try again. Guesses left: " + str(guesses_left)
            current_guess = raw_input("What word should fill in the blank(s) \
                for " + "___" + str(blank_number) + "___" + "? :").lower()
        else:
            print "YOU LOSE! GOOD DAY, SIR!"

# Win Condition
if blank_number == len(answers):
    print " "
    print "Completed phrase:"
    correct(blank_number, current_guess)
    print current_phrase
    print " "
    print "Congratulations!!!!... You won!"
