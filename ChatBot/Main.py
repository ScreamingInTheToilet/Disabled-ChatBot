print('Say anything to me. Either if it make sense or not.')

from AI import talk, remind
import time
import random

# Importing from libraries and files
random_time = random.randint(1, 3)
# Looping conversations
while True:
    response = input(str('')).lower()
    list_l = response.split()
    # response of the user is splitted into a list full of string variables so the bot can create a response.
    time.sleep(random_time)
    
    print(talk(response))
    time.sleep(random_time)
    remind()
#Since it is always True, if you run the code then your conversation will continue forever unless you stop running the code