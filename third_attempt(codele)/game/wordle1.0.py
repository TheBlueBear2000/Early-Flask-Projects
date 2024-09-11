from random import randint
import guizero as gui

CURRENT_DIR = "games/pythongames/wordle/"
MAX_ATTEMPTS = 6

app = gui.App(title = "Codele!")

# Define the printing board method
def printBoard(wordAttempts, description, keyboard, wordLength):
    printString = ""
    printString += "       CODELE\n\n"
    for i in range(MAX_ATTEMPTS):
        if i < len(wordAttempts):
            printString += "{:^20}\n".format(wordAttempts[i])
        else:
            newLine = ""
            for i in range(wordLength):
                newLine += "*"
            printString += "{:^20}\n".format(newLine)
            
    printString += "\n({}/{}) attempts\n\n".format(len(wordAttempts), MAX_ATTEMPTS)
    
    for line in keyboard:
        stringLine = ""
        for char in line:
            stringLine += char
        printString += "{:^20}".format(stringLine)
    printString += f"\n{description}\n"
    printString += f"{wordLength} letters\n"
    
    message.value = printString
    

def swapKey(char, keyboard, toReplace):
    for lineI in range(len(keyboard)):
        for charI in range(len(keyboard[lineI])):
            if char == keyboard[lineI][charI]:
                keyboard[lineI][charI] = toReplace
                return keyboard
    
# Take inputs
def inputtedWord(input, keyboard, letters):
    progress = ""
    if word.lower() == input.lower():
        return True, progress, keyboard
    else:
        for Ichar, char in enumerate(list(input)):
            if list(input)[Ichar] == letters[(min(len(letters)-1, Ichar))]:
                progress += char.upper()
                swapKey(char, keyboard, char.upper())
            elif char in letters:
                progress += char.lower()
                swapKey(char, keyboard, char.upper())
            else:
                progress += "*"
                swapKey(char, keyboard, " ")
                  
    return False, progress, keyboard

def tryWord():
    won, newLine, keyboard = inputtedWord(inputBox.value.lower(), keyboard, letters)
    

# Main loop
again = True
while again:
    keyboard = [list("qwertyuiop"),list("asdfghjkl"),list("zxcvbnm")]
        
    wordAttempts = []
    
    # Open the file and create the words and descriptions lists
    with open(CURRENT_DIR + "Keywords.txt", 'r') as linesFile:
        lines = linesFile.readlines()
        index = randint(0, len(lines)//2)
        word = lines[index * 2].lower()[:-1]
        description = lines[index * 2 + 1]
        description = description[0].upper() + description[1:]
    letters = list(word)
    
    # Setup
    message = gui.Text(app, text="")
    inputBox = gui.TextBox(app)
    inputButton = gui.PushButton(app, text="Try word", command=tryWord)
    wordProgress = str(["*" for letter in letters]) # Fill all letters with *
    attempts = 0
    
    # Main gameloop
    won = False
    while attempts < MAX_ATTEMPTS and not won:
        attempts += 1
        printBoard(wordAttempts, description, keyboard, len(letters))
        wordAttempts.append(newLine)
        
    # Win conditions
    endString = ""
    if won:
        endString += "Victory!"
    else:
        endString += "Too bad, you ran out of turns..."
    endString += "\nThe word was {}\n".format(word.capitalize())
    
    endString += "Would you like to play again? (y/n)    "
    message.value = endString
    
    # Check for replay
    rawAgain = ""
    while True:
        if rawAgain.lower() == "y":
            again = True
            break
        if rawAgain.lower() == "n":
            again = False
            break
        print("Please input either Y or N")
        
# 83 lines of code lesgo (Ignoring comments)