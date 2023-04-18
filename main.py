# importing random library
import random


# function to read text file and return an array of the lines in the file
def readTextFile():
    f = open("quotes.txt", "r")
    quotes = f.readlines()
    return quotes


# function that uses random library to choose a random quote from the array and print it
def printRandomQuote():
    quotes = readTextFile()
    randomQuote = random.choice(quotes)
    while randomQuote == "" or randomQuote == " ":  # if the quote is empty choose a new quote
        randomQuote = random.choice(quotes)
    print(randomQuote)


# function to add a new quote to the file
def addQuote():
    f = open("quotes.txt", "a")
    quote = input("Enter a quote: ")
    f.write("\n" + quote)


# program flow: asks user for input between 1 & 2, if 1 - then a random quote is printed, if 2 then user adds a quote
if __name__ == '__main__':
    print("RANDOM QUOTES!" + "\n")
    choice = int(input("Press 1 and enter for a random quote, or press 2 and enter to add a quote: "))
    if choice == 1:
        printRandomQuote()
    elif choice == 2:
        addQuote()
    else:
        print("Not a valid choice! Try again.")

