#######################
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
from data import Data,BulkNumber



#This is the url of strawpoll
url = 'https://www.strawpoll.me/'

#Here we get the data that we have defined in
#data.py (You can change it in data.py)
data = Data()
body =data


#This is how many 'cool' Id's we got in this run
coolNumber =0

# We define here the Function that sends 
# a post request to Strawpoll.me
def post_poll():
    r = requests.post(url, data=body)

    #For a ~4% performance boost you can remove the print(r.text) underneath here
    print('https://strawpoll.me/'+r.text[29:36])
    # this maybe looks weird, but somehow we have to
    # check the poll Number and decide if we want to
    # save  the  id into  data.py  (the text file we 
    # want to save special Poll Numbers
    if  r.text.count('0000000') >= 1 or r.text.count('1111111') >= 1 or r.text.count('2222222') >= 1 or r.text.count('3333333') >= 1 or r.text.count('4444444') >= 1 or r.text.count('5555555') >= 1 or r.text.count('6666666') >= 1 or r.text.count('777777') >= 1 or r.text.count('888888') >= 1 or r.text.count('999999') >= 1:
        print(r.text)
        f = open("requests.txt", "a")
        f.write(r.text+'\n')
        f.close()
        coolNumber+=1


print('I will create : ' +str(BulkNumber) + ' Polls')
sleep(2)
# Here we use Mulithreading to send the post requests
# as fast as possible
with concurrent.futures.ThreadPoolExecutor() as executor:
    for i in range(BulkNumber):
        executor.submit(post_poll)

print('I\'m done with creating ' +str(BulkNumber) + ' Polls')
print('I have saved ' +str(coolNumber) +' cool ID\'s')