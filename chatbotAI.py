def response(bot):
    if bot.lower() == "hello":
        print("Hey There!")

    elif bot.lower() == "how are you?":
        print("Im great thanks!")

    elif bot.lower() == "help":
        print("I can help you with whatever you need!")

    else:
        print("I do not undertsand")
    
while True:
    #Chatbot asking you what you need
    bot = input("What can I help you with?")
    
    if bot.lower() == "quit":
        print("Goodbye!")
        break

    response(bot)