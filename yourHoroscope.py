""""
Ask the user for their star sign
2
Validate the input — if they type something that isn't a real star sign, tell them and ask again
3
Randomly assemble a horoscope from separate lists — one for mood, one for a prediction, one for lucky number
4
Print a personalised horoscope using their sign and the random elements
5
Use at least 2 functions

"""
import random

#variable with the list of all horoscopes
signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra"
             , "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

#varibale with kinds of moods
mood = ["Angy", "Sad", "Flustered", "Ecstatic", "Calm"]

# list of the predictions 
predictions = ["You will fight a bear!", "You won't get a Victory Royale", "A red light will annoy you", 
               "You will receive great news today!", "You will be relaxin maxxin"]


 #generates a random integer from the range
lucky_num = random.randint(1, 10000)

#defining get_Horoscope as a funciton
def get_Horoscope():
    yourHoroscope = ""
    #while the input is not what shows in signs, you get invalid response
    while yourHoroscope not in signs:
          yourHoroscope = input("What is your Horoscope? ").title()
          print("Invalid Horoscope. Please input a valid Horoscope.")

    #prints valid response 
    print(f"OMG! You are {yourHoroscope}! I have a prediction and a lucky number for you today! I will guess your mood as well")

    #generating a random choice from the list "mood" and printing out how you're feeling
    feelings = random.choice(mood)
    print(f"You are {feelings} today. I can feel it in my nuggets.")

    #prints out a random integer from the range
    print(f" Your lucky number today is {lucky_num:,}! Sieze the world with your number :)")

    prediction = random.choice(predictions)
    print(f"Your prediction for today is: {prediction}")
    return yourHoroscope

def predict(): 
     return
get_Horoscope()

