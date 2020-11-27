#
#######################
# Straw Poll Bulk Bot #
# @CodeChrisB         #
#######################
# You can change the Questions and Answers underneath
# Keep in mind that the quotation marks --> "" are 
# necessary, and should not be removed.
#If you only want 2 answers leave the others blank --> ""
YourQuestion = "How many Numbers are there?"
FirstAnswer ="Infinite"
SecondAnswer ="None at all"
ThridAnswer ="42"
FourthAnswer =""
FifthAnswer =""
SixthAnswer =""
SeventhAnswer = ""
EighthAnswer = ""
NinthAnswer = ""
BulkNumber =1000000000 # How often do you want to send your question?



###########################
#      Do not change      #
#  the values underneath. #
###########################
body = {
    "poll-title": YourQuestion,
    "options-option-1": FirstAnswer,
    "options-option-2": SecondAnswer,
    "options-option-3":ThridAnswer,
    "options-option-4": FourthAnswer,
    "options-option-5": FifthAnswer,
    "options-option-6": SixthAnswer,
    "options-option-7": SeventhAnswer,
    "options-option-8": EighthAnswer,
    "options-option-9": NinthAnswer,
    "f154f5e7fac7ead116b8382d45a2fe8d9": "y",
    "poll-submit": "create"
}

         
# ######################
# Straw Poll Bulk Bot #
# @CodeChrisB         #
#######################
# This bot is free to use you do not have to credit me or anything else
# just take it and what you want.
# If you want to change the question and answers
# Check out the data.py file

# Why to use this bot?
# Strawpoll saves their polls with Id's they always add +1 for the next Poll
# If we want to get a specific Poll Number like https://strawpoll.me/22222222
# We can just Spam a lot of Polls to get to this Number. I have calculated that
# This Bot can create 250.000 Polls per Hour. (Atleast on my Pc)



import requests
import concurrent.futures
from time import sleep

print('Start Bot')

#This is the url of strawpoll
url = 'https://www.strawpoll.me/'

# We define here the Function that sends 
# a post request to Strawpoll.me
def post_poll():
    requests.post(url, data=body)

with concurrent.futures.ThreadPoolExecutor() as executor:
    for i in range(BulkNumber):
        executor.submit(post_poll)