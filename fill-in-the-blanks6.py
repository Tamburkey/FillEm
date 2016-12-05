# IPND Stage 2 Final Project
import sys

# Easy start phrase - taken from starter code
current_phrase_list = [
"A common first thing to do in a language is display\n\
'Hello ___1___!'  In ___2___ this is particularly easy; all you have to\n\
do is type in: ___3___ 'Hello ___1___!'\n\
\n\
Of course, that isn't a very useful thing to do. However, it is an \n\
example of how to output to the user using the ___3___ command, and \n\
produces a program which does something, so it is useful in that \n\
capacity.\n\
\n\
It may seem a bit odd to do something in a Turing complete language \n\
that can be done even more easily with an ___4___ file in a browser,\n\
but it's a step in learning ___2___ syntax, and that's really its \n\
purpose.",

# Medium start phrase - taken from starter code
"A ___1___ is created with the def keyword. You specify the inputs\n\
a ___1___ takes by adding ___2___ separated by commas between the\n\
parentheses.\n\
\n\
___1___s by default return ___3___ if you don't specify the value to \n\
return.___2___ can be standard data types such as string, number, \n\
dictionary, tuple,and ___4___ or can be more complicated such as \n\
objects and lambda functions.",
# Hard start phrase - taken from Monty Python
"We're knights of the round ___1___. We dance when e're we're \n\
___2___. We do routines, and chorus-scenes, with footwork ___3___. We \n\
dine well here in ___4___. We eat ___5___, and ___6___, and ___7___ a \n\
lot.\n\
\n\
We're knights of the round ___1___. Our shows are ___8___. But many \n\
times,we're given rhymes, that are quite ___9___. We're opera mad in \n\
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


def guess_pick(b):
    """Take in input (b), validate as int, and return integer (guesses_left)"""
    global guesses_left
    while is_number(b) == False:
        print "Try a number this time. "
        b = (raw_input("Choose the number of guesses before you \
    lose."))
    if b <= 0:
        print "YOU LOSE! GOOD DAY, SIR!"
        sys.exit()
    b = int(b)
    guesses_left = b
    return guesses_left


def new_game(a, b, c):
    """Takes in initial game state variables (a), (b), and (c) and displays new
    game start"""
    print "You have chosen: " + a
    print " "
    print "You will get " + str(b) + " guesses per problem."
    print " "
    print "Current phrase:"
    print c


def play(c, d):
    """Take in integers (c) and (d), loops over them prompting user for input
    while updating (c) and (d), return updated integer (blank_number)"""
    global current_phrase
    global answers
    global current_guess
    global blank_number
    while c > 0 and d < len(answers):
        if current_guess == answers[d-1]:  # Correct input
            print "Correct answer!"
            print " "
            correct(d, current_guess)
            print "Current phrase:"
            print current_phrase
            d += 1
            current_guess = raw_input("What word should fill in the blank(s) \
for " + "___" + str(d) + "___" + "? :").lower()
        else:  # Incorrect input
            c -= 1
            if c == 1:
                print "Wrong answer, try again. Guesses left: " + \
                str(c) + " Make it count!"
                current_guess = raw_input("What word should fill in the blank(s) \
for " + "___" + str(d) + "___" + "? :").lower()
            elif c > 0:
                print "Wrong answer, try again. Guesses left: " + str(c)
                current_guess = raw_input("What word should fill in the blank(s) \
for " + "___" + str(d) + "___" + "? :").lower()
            else:
                print "YOU LOSE! GOOD DAY, SIR!"
    blank_number = d
    return blank_number


def win(a):
    """Take in integer (a), compare to len(answers), update and print
    (current_phrase) """
    global current_phrase
    global blank_number
    global current_guess
    global answers
    if a == len(answers):
        print " "
        print "Completed phrase:"
        correct(blank_number, current_guess)
        print current_phrase
        print " "
        print "Congratulations!!!!... You won!"


""" START OF GAME - Difficulty selection"""
diff_input = raw_input("Choose a difficulty: easy, medium, or hard. \
Incorrect input will result in a loss.").lower()

difficulty(diff_input)  # Returns current phrase and answers for difficulty

guesses_left = (raw_input("Choose the number of guesses before you \
lose."))

guess_pick(guesses_left)  # Validates and returns number of guesses left

new_game(diff_input, guesses_left, current_phrase)  # Displays new game state

current_guess = raw_input("What word should fill in the blank(s) for " + 
"___" + str(blank_number) + "___" + "? :").lower()  # First guess

play(guesses_left, blank_number)  # Start of standard game loop

win(blank_number)  # Win condition
