import random
import fileinput
import re
import tweepy


# This is where i set my api tokens for twitter
consumer_key ="<your consumer key>"
consumer_secret ="<your consumer secret>"
access_token ="<your access token>"
access_token_secret ="<your access token secret>"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

loop = 1
while loop ==1:
    
    #setting regex
    pattern = re.compile("^\S")

    #import the script
    script = open("shrek.txt").read()

    #generate a random number out of the lines to select
    randomnumber = int(random.randint(0,3430))

    #Select a random line from the file 
    data = []

    with open("shrek.txt","r") as f:
        data = f.readlines()
        randomline = data[randomnumber]
        

    # is string empty  
    if re.match(pattern,randomline):
        message = randomline
        loop = 2
        break
    else:
        loop = 1


# update the status 
api.update_status(status = message)





        



    








