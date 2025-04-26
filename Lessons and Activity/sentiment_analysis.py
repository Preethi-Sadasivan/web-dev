from textblob from Textblob

print  ("Welcome to the mood detector")

name = input ("Hi.. May I know your name")
print(f"Hi {name}. Lets find out the mood of your sentence")
print ("type exit to exit the program ")


while(True):
    sentence = input ("Enter your sentence")

    if (sentence == "exit"):
        print("Bye for now")
        break

    blob = textblob(sentence)
    sentiment = blob.sentiment.polarity

    if sentiment < 0:
        print ("Negative Emotion")
    elif sentiment > 0:
        print ("Positive Emotion")
    else:
        print ("Neutral Sentiment")
