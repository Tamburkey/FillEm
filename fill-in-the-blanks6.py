# IPND Stage 2 Final Project
import sys
global cp

# Easy start phrase - taken from starter code
cp_e = '''A common first thing to do in a language is display
'Hello ___1___!'  In ___2___ this is particularly easy; all you have to do
is type in: ___3___ "Hello ___1___!"

Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the ___3___ command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an ___4___ file in a browser, but it's
a step in learning ___2___ syntax, and that's really its purpose.
'''

# Medium start phrase - taken from starter code
cp_m = '''A ___1___ is created with the def keyword. You specify the inputs
a ___1___ takes by adding ___2___ separated by commas between the parentheses. 

___1___s by default return ___3___ if you don't specify the value to return. 
___2___ can be standard data types such as string, number, dictionary, tuple, 
and ___4___ or can be more complicated such as objects and lambda functions.
'''

# Hard start phrase - taken from Monty Python
cp_h = '''We're knights of the round ___1___. We dance when e're we're ___2___. 
We do routines, and chorus-scenes, with footwork ___3___. We dine well here in ___4___.
We eat ___5___, and ___6___, and ___7___ a lot.

We're knights of the round ___1___. Our shows are ___8___. But many times, we're given
rhymes, that are quite ___9___. We're opera mad in ___4___. We sing from the ___10___ a lot.
'''

rn = 1 # guessing round number
answers = [["world", "python", "print", "html"], ["function", "arguments", "None", "list"], ["table", "able", "impeccable", "Camelot", "ham", "jam", "spam", "formidable", "unsingable", "diaphragm"]]

# word_in_pos is a helper function from mad_libs quiz to preserve punctuation
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
# correct is a function takes in a number (num), and a second string (guess), and replaces all (num) blanks with the (guess) and returns an updated string (cp)
def correct(num, guess): 
    global cp
    rep = [] #replacement list
    blank = "___" + str(num) + "___" 
    for word in cp.split(' '):
        replacement = word_in_pos(guess, answ)
        if replacement != None:
            word = word.replace(blank, guess)
            rep.append(word)
        else:
            rep.append(word)
        cp = ' '.join(rep)
    return cp

### START OF GAME 

# Difficulty selection
diff = raw_input("Choose a difficulty: easy, medium, or hard. Incorrect input will result in a loss. ")
if diff == "easy":
    answ = answers[0]
    cp = cp_e
elif diff == "medium":
    answ = answers[1]
    cp = cp_m
elif diff == "hard":
    answ = answers[2]
    cp = cp_h
else:
    print "INVALID SELECTION! YOU LOSE! GOOD DAY, SIR!"
    sys.exit()

gl = int(raw_input("Choose the number of guesses before you lose."))

print "You have chosen: " + diff
print " "
print "You will get " + str(gl) + " guesses per problem."
print " "
print "Current phrase:"
print cp

# First guess
ci = raw_input("What word should fill in the blank(s) for "+"___" + str(rn) + "___" +"? :")

# Start of standard game loop
while gl > 0 and rn < len(answ):
# Correct input   
    if ci == answ[rn-1]: 
        print "Correct answer!"
        print " "
        correct(rn, ci)
        print "Current phrase:"
        print cp
        rn += 1
        ci = raw_input("What word should fill in the blank(s) for "+"___" + str(rn) + "___" +"? :")
        if rn == len(answ):
            print "Congratulations!!!!... You won!"
# Incorrect input
    else: 
        gl -= 1
        if gl == 1:
            print "Wrong answer, try again. Guesses left: " + str(gl) + " Make it count!"
            ci = raw_input("What word should fill in the blank(s) for "+"___" + str(rn) + "___" +"? :")
        elif gl > 0:
            print "Wrong answer, try again. Guesses left: " + str(gl)
            ci = raw_input("What word should fill in the blank(s) for "+"___" + str(rn) + "___" +"? :")
        else:
            print "YOU LOSE! GOOD DAY, SIR!"



