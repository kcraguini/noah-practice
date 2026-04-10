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
# prints out zodiac moods by signs
def zodiac_mood():
     emotion = input().lower()
     match emotion:
          case "Water":
           print("(Cancer, Scorpio, Pisces) You are deeply sensitive and often moody")
           
          case "Fire":
           print("(Aries, Leo, Sagittarius) You tend to be dramatic or irritable")

          case "Earth":
             print("(Taurus, Virgo, Capricorn) You can handle stress with practical, often inward reactions")
          case "Air":
             print("(Gemini, Libra, Aquarius) You tend to detach")

          case _:
             print("You picked an invalid Zodiac Mood :c")
             zodiac_mood()
     return 
# these are the signs of every horoscope
signs = [
     "aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius",
    "capricorn", "aquarius", "pisces"
    ]

yourHoroscope = input("What is your Horoscope? ").lower()

if yourHoroscope in signs:
     print (yourHoroscope.capitalize())
else:
     print("Unknown Horoscope")

