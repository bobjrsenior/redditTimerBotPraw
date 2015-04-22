from pprint import pprint
import time
import praw
import re
import datetime

def timeTil(): #Returns a formatted length until the event
     td = datetime.datetime(year, month, day, hour, minute, second) - datetime.datetime.now()
     days = td.days
     hours = int(td.seconds / 3600)
     minutes = int(td.seconds / 60) - (hours * 60) 
     return keyword + ': ' + str(days) + 'd:' + str(hours) + 'h:' + str(minutes) + 'm' + endKeyword

user_agent = ("Timer tests v0.1.4 by /u/bobjrsenior") #Let reddit know who you are
r = praw.Reddit(user_agent=user_agent)
r.login(input('Username: '), input('Password: ')) #Input username, pass here
subredditName = input('Subreddit Name: ') #Name of the subreddit
subreddit = r.get_subreddit(subredditName)  #get the subreddit
updateSpeed = 60 #Update the timer every _ seconds

#get inputs for dates and such
keyword = input('Keyword in sidebar to find: ')
endKeyword = input('Keyword that marks the end of the countdown (\\\\n if new line): ')
year = int(input('Year: '))
month = int(input('Month: '))
day = int(input('Day: '))
hour = int(input("Hour (0 if it's not a hourly specific event): "))
minute = int(input("Minute (0 if it's not a minutely specific event): "))

while True: #Infinite Loop since it is a bot
    settings = r.get_settings(subredditName) #Get the subreddits settings
    description = settings['description'] #Get the sidebar
    #Update the countdown in the sidebar
    description = re.sub(keyword + ':.*' + endKeyword, timeTil(), description, 1)
    #Update the subreddit
    r.update_settings(subreddit , description=description)
    #Sleep until we need to update again
    time.sleep(updateSpeed)
