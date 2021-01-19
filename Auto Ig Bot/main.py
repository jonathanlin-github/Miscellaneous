from InstagramAPI import InstagramAPI
from time import sleep
import time
import random
import datetime


api = InstagramAPI('username','password')
api.login()

all_names = ['therock','kyliejenner','kendalljenner','kevinhart4real','cristiano','chrishemsworth','robertdowneyjr','leomessi','justinbieber','jlo','kimkardashian','kourtneykardash','iamcardib','snoopdogg','kingjames','champagnepapi','postmalone','krisjenner','arianagrande','selenagomez','dualipa','camila_cabello','billieeilish','taylorswift','gigihadid','ddlovato']

names = ['therock','kyliejenner','kendalljenner','kevinhart4real','cristiano','chrishemsworth','robertdowneyjr','leomessi','justinbieber','jlo','kimkardashian','kourtneykardash','iamcardib','snoopdogg','kingjames','champagnepapi','postmalone','krisjenner','arianagrande','selenagomez','dualipa','camila_cabello','billieeilish','taylorswift','gigihadid','ddlovato']

def sleeep(time):
    bottom = int(time*60*.75)
    top = int(time*60*1.75)
    number = random.randint(bottom,top)
    sleep(number)


action_counter = 0

start_time = time.time()
while True:
    if len(names) <= 2:
        names = all_names
    
    name = random.choice(names)
    names.remove(name)


    api.searchUsername(name)
    result = api.LastJson
    user_id = result['user']['pk']
    api.follow(user_id)
    print('Followed @' + name)
    print('Sleeping for 3 min')
    sleeep(3)

    api.unfollow(user_id)
    print('Unfollowed @' + name)
    print('Sleeping for 5 min')
    action_counter = action_counter + 1
    print('Celebs interacted with: ' + str(action_counter))

    seconds = time.time() - start_time
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    print('Time Elapsed: ' + str(int(h)) + 'h ' + str(int(m)) + 'm ' + str(int(s)) + 's')
    sleeep(5)
    print('')