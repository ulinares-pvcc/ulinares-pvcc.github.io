# Name: Uzziel Vea-Linares
# Program Purpose: Pordle (PVCC Wordle): Word Guessing Game
#   The Program chooses a random word from a file of words. The user tries to
#   figure out the woed in the fewest guesses by guessing letters in the word.
#   This program uses an input FILE, LISTS, and STRING SLICES (section of the string)

import random
wordList = []
inFile = "animals.txt"
global wordFile

def main():
    global wordList, inFile
    playAgain = True
    while playAgain:
        printHeadings()
        printMenu()
        wordList = []
        wordFile = open(inFile, "r")
        for textLine in wordFile:
            for word in textLine.split():
                wordList.append(word)
        wordFile.close()
   
        playGame()
        yesno = input("Would you like to play again? (Y/N) ")
        if yesno == "n" or yesno == "N":
            playAgain = False;
            print("Thank you for playing PORDLE!")
            return()
        
def printHeadings():
    print("\nWelcome to PORDLE! The PVCC Wordle Game")
    print("I will think of a word and you try to guess the letters in the word.")
    print("The number of dashes indicates the number of letters in the word.")
    
def printMenu():
    global inFile
    print("\nChoose a PORDLE category:")
    print("\t1. Animals")
    print("\t2. Names")
    print("\t3. Colors")
    print("\t4. Sports")
    category = input("Please enter the category number: ")
    
    if category == "1":
        inFile = 'animals.txt'
    elif category == "2":
        inFile = 'names.txt'
    elif category == "3":
        inFile = 'colors.txt'
    elif category == "4":
        inFile = 'sports.txt'
    else:
          inFile = 'animals.txt'
          print("This will be an ANIMAL Pordle")
        
def playGame():
    numguesses = 1
    letterUsed = []
    
    wordChosen = random.choice(wordList)
    pordle = wordChosen
    for i in range (len(pordle)):
        pordle = pordle[0:i] + "_" + pordle[i+1:]
    print (" ".join(pordle))
        
    while pordle != wordChosen:
        letterGuess = input("Please enter a letter: ")
        letterGuess = letterGuess.lower()
        letterUsed.append(letterGuess)
        print ("Number of Guesses: " + str(numguesses))
        
        for i in range(len(wordChosen)):
            if wordChosen[i] == letterGuess:
                pordle = pordle[0:i] + letterGuess + pordle[i+1:]
                
        print("Used letter: ")
        print(letterUsed)
        print(" ".join(pordle))
        numguesses += 1
        
    print("Well done! You guessed in " + str(numguesses-1) + " guesses!")

main()
