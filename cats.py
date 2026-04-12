import random


cats = {
    0 : {
       "catType" : "tabby", 
       "lifeSpan" : 15,
       "color" : ["gray", "orange", "black"] 
    },

    1: {
       "catType" : "siamese",
       "lifeSpan" : 500,
       "color" : ["brown", "caca", "filipino brown"]
    },

    2: { 
        "catType" : "egyptian baldie",
        "lifeSpan": 88,
        "color" : ["red", "black", "lavender"]
    },
    3: { "catType": "calico",
        "lifeSpan" : 6,
        "color" : ["green"]
    },
    4:  {"catType" : "britsh shorthair",
         "lifeSpan" : 5,
         "color" : ["pink"]
    }
}

def spacers():
    for _ in range(15):
        print("* ", end="")
    print("")

def typeOfCat():
   poopoo = random.choice(cats)
   spacers()
   print(f"I recommend this cat type:  {poopoo["catType"]}")
   print(f"I also recommend this color: {poopoo["color"]}")
   print(f"This is their average lifespan: {poopoo["lifeSpan"]}")
   spacers()
typeOfCat()