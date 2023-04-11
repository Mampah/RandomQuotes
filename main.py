import random


def readTextFile():
    f = open("quotes.txt", "r")
    quotes = f.readlines()
    return quotes


def printRandomQuote():
    quotes = readTextFile()
    randomQuote = random.choice(quotes)
    while randomQuote == "" or randomQuote == " ":
        randomQuote = random.choice(quotes)
    print(randomQuote)


def addQuote():
    f = open("quotes.txt", "a")
    quote = input("Enter a quote: ")
    f.write("\n" + quote)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("RANDOM QUOTES!" + "\n")
    choice = int(input("Press 1 and enter for a random quote, or press 2 and enter to add a quote: "))
    if choice == 1:
        printRandomQuote()
    elif choice == 2:
        addQuote()
    else:
        print("Not a valid choice! Try again.")

