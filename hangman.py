# Hangman Game

# Random words(nouns) / 10 lives, try your guessing skills!

import re
import time
import urllib.request

randomWord = urllib.request.urlopen('https://random-word-form.herokuapp.com/random/noun/a').read().decode('utf-8')

def newGame(providedLives, word):
    lives = providedLives
    wordStr = word.lower()
    wordArray = list(wordStr)
    arrayToFill = ['_'] * len(list(wordStr))
    wrongLetters = []
    correct = False


    def showInfo():
        print('Current word: {}'.format(arrayToFill))
        print('Wrong letters: {}'.format(wrongLetters))
        print('Remaining lives: {}'.format(lives))


    while lives > 0:
        userInput = input('\n\nInput a letter:\n').lower()
        if len(userInput) > 1:
            print('Please provide 1 letter only')
            time.sleep(1)
        if not re.match(r"^[A-Za-z]+$", userInput):
            print('Alphabetic letters only!')
        else:
            for i in range(len(arrayToFill)):
                if wordArray[i] == userInput:
                    arrayToFill[i] = userInput
                    showInfo()
                    correct = True

            if correct:
                print('Correct!')
                correct = False
            else:
                correct = False
                if userInput not in wrongLetters:
                    wrongLetters.append(userInput)
                    lives = lives - 1
                    showInfo()
                else:
                    showInfo()

                print('Wrong!')

            if wordArray == arrayToFill:
                print('\nCongratulations, you won!')
                time.sleep(3)
                print('\nStarting a new game...')
                time.sleep(1)
                print('\n\n.....................')
                randomWord = urllib.request.urlopen('https://random-word-form.herokuapp.com/random/noun/a').read().decode('utf-8')
                newGame(providedLives, randomWord)

            if lives == 0:
                print('No more lives left :(')
                time.sleep(3)
                print('\nStarting a new game...')
                time.sleep(1)
                print('\n\n.....................')
                randomWord = urllib.request.urlopen('https://random-word-form.herokuapp.com/random/noun/a').read().decode('utf-8')
                newGame(providedLives, randomWord)

newGame(10, randomWord)