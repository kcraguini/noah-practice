#importing Natural Language ToolKit
import nltk
#downloading 'punkt_tab' which is essentially a language file from the internet.
nltk.download('punkt_tab')
#grabbing one tool from the toolbox NLTK
from nltk.tokenize import word_tokenize

#creating a funciton that will tokenize what the user inputs "reading the input based off keywords"
def tokensizer(bot):
    tokens = word_tokenize(bot)
    return tokens

def response(tokens):
    if "hello" in tokens:
        print("Hey There!")

    elif "how are you?" in tokens:
        print("Im great thanks!")

    elif "help" in tokens:
        print("I can help you with whatever you need!")

    else:
        print("I do not undertsand")
    
while True:

    #Chatbot asking you what you need
    bot = input("What can I help you with?")

    if bot.lower() == "quit":
        print("Goodbye!")
        break
    #calling the tokenizor function and setting the parameter to "bot", so it reads your input
    tokens = tokensizer(bot)
    response(tokens)