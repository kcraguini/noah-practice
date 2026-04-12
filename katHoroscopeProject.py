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

# This is a nested dictionary. This will hold different moods and predictions
horoscopeMap = {
    0 : {
        "mood" : "Blissful",
        "prediction" : "Today will be a breeze. So stop and smell the roses!"
    },
    1 : {
        "mood" : "Lazy",
        "prediction" : "You will have a great day being a couch potato :p"
    },
    2 : {
        "mood" : "Happy",
        "prediction" : "You're loved ones will bring you joy today!"
    },
    3 : {
        "mood" : "Moody",
        "prediction" : "You will be inconvience today. Like stub your toe or get a paper cut"
    },
    4 : {
        "mood" : "Sad",
        "prediction" : "You will have a bad day. Maybe you will lose your phone or something. idk don't ask me bruh"
    },
    5 : {
        "mood" : "Angry",
        "prediction" : "Someone called you a chud like Noah. You will be very mad and want to fight them. C h u d"
    }

}

# Creates the random number in a certain range
def randomize(n):
    return random.randrange(0, n)

# function to make a stars gap cause I'm to lazy to type it out
def starMaker():
    for _ in range(30):
        print("* ", end="")
    print("")


# prints out zodiac moods by signs
def zodiac_mood():
    print("This is what the star are saying for you today")
    starMaker()

    # grabs a random number from 0 to the size of the arr
    dictRandomNum = randomize(len(horoscopeMap))
    # print(dictRandomNum)
    print(f"You're mood will be today {horoscopeMap[dictRandomNum]["mood"]}")
    print(f"I predict ... {horoscopeMap[dictRandomNum]["prediction"]}")
    print(f"You're lucky number for today is {randomize(1000)}")

    starMaker()
    return

# these are the signs of every horoscope
signs = [
    "aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius",
    "capricorn", "aquarius", "pisces"
    ]

# Initialize yourHoroscope outside of the while loop
yourHoroscope = ""

# Created a while loop so that it will ask again if the horoscope is invalid
while (True):
    yourHoroscope = input("What is your Horoscope? ").lower()
    # yourHoroscope = "cancer" # for testing purposes
    if yourHoroscope in signs:
        print(f"\nOh my goodness! You're a {yourHoroscope.capitalize()}. The stars are aligning today")
        zodiac_mood()
        break
    else:
        print("Unknown Horoscope")

