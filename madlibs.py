import random, time

def make(a, b, c, d):
    sentences = [
        f"It was a {c}, cold November day...",
        f"After hiding the painting in his {a} for two years...",
        f"He grew {c} and tried to sell it to a/an {a} in Florence...",
        f"The {a} {c} fox {b} over the {c} dog"
    ]
    rsentences = random.choice(sentences)
    return rsentences

while True:
    x = input("--Madlibs--\nPlay | Exit\n").lower()
    if x == "play":
        print("Let's get some variables!")
        #getting a noun
        noun = input("Noun: ")
        #getting a verb
        verb = input("Verb: ")
        #getting an adjective
        adjective = input("Adjective: ")
        #getting an adverb
        adverb = input("Adverb: ")
        time.sleep(0.2)
        print(make(noun, verb, adjective, adverb))
        time.sleep(0.2)
    elif x == "exit":
        break
    else:
        print("Command doesn't exist!")