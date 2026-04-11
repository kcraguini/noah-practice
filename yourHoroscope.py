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

#defining get_Horoscope as a funciton
def get_Horoscope():
    yourHoroscope = input("What is your Horoscope? ").title()
    #while the input is not what shows in signs, you get invalid response
    while yourHoroscope not in signs:
          print("Invalid Horoscope. Please input a valid Horoscope.")
          yourHoroscope = input("What is your Horoscope? ").title()

    #prints valid response 
    print(f"OMG! You are a {yourHoroscope}! I have a prediction and a lucky number for you today! I will also guess your mood")

    #calling the function "predict()" so it runs within this function
    predict()

    #generates a random integer from the range
    lucky_num = random.randint(1, 10000)
    #prints out a random integer from the range
    print(f"Your lucky number today is {lucky_num:,}! Sieze the world with your number :)")

    #generating a random choice from the list "mood" and printing out how you're feeling
    feelings = random.choice(mood)
    print(f"You are {feelings} today. I can feel it in my nuggets!")
    return yourHoroscope


def predict(): 
     predictions = ["You will fight a bear!", "You won't get a Victory Royale", "A red light will annoy you", 
               "You will receive great news today!", "You will be relaxin maxxin"]
     #using a random choice from the list predication and printing/ returning it to the user
     random_prediction = random.choice(predictions)
     print(f"This is your random prediction: {random_prediction}")
     return random_prediction
#calling the function get_Horoscope so that the entire code works
get_Horoscope()