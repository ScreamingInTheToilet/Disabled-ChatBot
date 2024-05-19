# import modules for the Chatbot.
import random
import json
import time
import random
from Jokes import List_joke

# To read data from a seperate file.

filename = r'C:/Users/dell/OneDrive - Nord Anglia Education/AnhKhoaProgramming/ChatBot/storage.json'
# A command that opens storange.py. storage.py is the memory of the bot.
with open(filename, 'r') as f:
  data = json.load(f)


# A function to return the user's name
def say_name():
  # for loop that checks different memorized topic
  for item in data['people']:
    # Item name is a list that contains the user's name.
    name = item['name']
    for i in name:
    # a condition which checks if the player has a name or not. if not then bot's response wouldn't contain the user's name.
      if name == []:
        return ''
      # if the user does have a name then bot returns with user's name by referencing variable "i"
      else: 
        return i

#list of bot's reply options
bot_greet = ['Hola', 'Bonjour', 'Hello there', 'Hey']
# random choice of reply options
bot_greet_ = random.choice(bot_greet)
# Block greet, define function greet
def greet(list):
  '''
  User_greet is a list that contains 3 dictionaries. Each dictionaries have string "say" and it corresponds with "response".
  Each item/dictionary is referenced using a forloop that calls them "i"
  Currently there are 3 items/dictionaries in the user_greet.
  '''
  User_greet = [
    {'Say': 'hello', 'response': bot_greet_},
    {'Say': 'hi', 'response': bot_greet_},
    {'Say': 'wassup', 'response': bot_greet_},

            ]

  for i in User_greet:
  # forloop loops until all dictionaries/items in list User_greet are referenced and checked.
    Say = i['Say']
    response = i['response']
    #key 'say' is referenced and corresponds to referenced 'response'
    Talk_chain = [{'Say': Say, 'response': response}]
    # you don't really need variable Talk_chain, it just creates the same dictionary.
    for x in list:
      if Say == x:
        for a in Talk_chain:
          response_ = a['response']
          return f'{response_} {say_name()} !'
          # return object greet as a variable, this is useful.
# A function to remember the user's name
def enter_name(list):
  # creates a list which stores different user sentence component when they are declaring their name.
  Starter_Sentence = [{'Arg1': 'my', 'Arg2': 'name', 'Arg3': 'is', 'Response': 'hello'}]

  def remove_starter(list):
    for i in Starter_Sentence:
      Arg1 = i['Arg1']
      Arg2 = i['Arg2']
      Arg3 = i['Arg3']
      for x in list:
        if x == Arg2:
          list.remove(Arg1)
          list.remove(Arg2)
          list.remove(Arg3)
          # removing Arg1, Arg2, Arg3 so the remaining item is the string containing the user's name
          return remember_name(list)
          # returning object remove_starter as variable remember_name(list)
  
  def remember_name(list):
    count = 0
    for item in data['people']:
      name = item['name']
      for i in name:
        count += 1
        # if there is a variable in name list from storage.py, then there will be an iteration and count is incremented by 1
      if count == 0:
      # if count variable is zero then there is no name, and bot will add a name in
        name.append(list[0])
        return f'Hello {list[0]}!'
      else:
      # if count variable is one, then the bot remembered the user's name. The bot will remove current name and replace it
      # with a new name that the user wished for.
        name.pop()
        #removes name using pop
        name.append(list[0])
        ''' 
        name of the user is list[0] or the first item in the list. The user initally had other items but is removed in
        remove_starter.
        ''' 
        #return remember_name as string variable "Hello name_of_user"
        return f'Hello {list[0]}!'
  
  return remove_starter(list)
  # return object enter_name as variable remove_starter which is remember_name which is 'Hello user_name'. This is basically a loop of define unctions
# A define function to response to a demand or a simple question from the user that begins with "Can you".

def question(list):

  Script_list = [
    {'Arg1': 'can', 'Arg2': 'you', 'Response': ['Yes I can', 'No I cannot', 'Sometimes I can']},
    {'Arg1': 'can', 'Arg2': 'i', 'Response': ['Yes you can', 'No you cannot', 'Sometimes you can']},
    {'Arg1': 'will', 'Arg2': 'you', 'Response': ['Yes I will', 'No I will not', 'Sometimes I will']},
    {'Arg1': 'would', 'Arg2': 'you', 'Response': ['Yes I would', 'No I would not', 'Sometimes I would']},
    {'Arg1': 'could', 'Arg2': 'you', 'Response': ['Yes I could', 'No I could not', 'Sometimes I could']},
    {'Arg1': 'are', 'Arg2': 'you', 'Response': ['Yes I am', 'No I am not', 'Sometimes I am']},
    {'Arg1': 'do', 'Arg2': 'you', 'Response': ['Yes I do', 'No I do not', 'Sometimes I do']}
    
  ]

  Word_swap = [
    {'Word': 'me', 'Swap': 'you'},
    {'Word': 'my', 'Swap': 'your'},
    {'Word': 'i', 'Swap': 'you'},
    {'Word': 'you', 'Swap': 'i'},

              ]
  
  # A define function that swaps pronouns between perspectives.
  def swap_pronoun(list):
    for i in Word_swap:
      Word = i['Word']
      Swap = i['Swap']
      Obj = [{'Word': Word, 'Swap': Swap}]
      for elements in list:
        if elements == Word:         
          count = list.index(Word)
          list.remove(elements)
          list.insert(count, Swap)
          

          
          
    
  def mark_removal(list):
    Mark_removal = ['.', '?', '!']
    for i in list:
      if i in Mark_removal:
        list.remove(i)
  
  mark_removal(list)

  def join_str(str):
    result = ''
    for s in str:
      result += ' ' + s
    return result[1:]
  
  def can_you(list):
    global Response__
    for x in Script_list:
        Arg1 = x['Arg1']
        Arg2 = x['Arg2']
        Response = x['Response']
        obj = [{'Arg1': Arg1, 'Arg2': Arg2, 'Response': Response}]
        if list[0] == Arg1 and list[1] == Arg2:
          ListA = [Arg1, Arg2]
          for b in ListA:
            list.remove(b)
          for item in obj:
            Response_ = item['Response']
            Response__ = random.choice(Response_)
          swap_pronoun(list)
          return f'{Response__} {join_str(list)}.'
          
        
  return can_you(list)
# A store function that stores the User's emotion.
def store(var):
  count = 0
  for i in data['people']:
    emotion = i['emotion']
    for i in emotion:
      count += 1
      if count != 0:
        emotion.pop()
        emotion.append(var)
      else:
        emotion.append(var)
# An emotion define function to give response to the person's emotion
def emotion(list):
  


  for item in data['people']:
    dictionary = item['dictionary']
    for category in dictionary:
      positive = category['positive']
      negative = category['negative']
  # A define function that allows the chatbot to learn new words.
  def store_vocab(var):
    print('I don\'t understand this word. Is it positive or negative?')
    Extra_input = input('').lower()
    time.sleep(1)
    Extra_input_list = Extra_input.split()
    for item in data['people']:
      dictionary = item['dictionary']
      for i in dictionary:
        positive = i['positive']
        negative = i['negative']
        for x in Extra_input_list:
          if x == 'positive':
            positive.append(var)
            return 'Thanks, learned a new word today !'
          elif x == 'negative':
            negative.append(var)
            return 'Thanks, learned a new word today!'
            


  def understand_emotion(list):
    for i in list:
      if i in positive:
        store(i)
        return f'Glad to know that you are {i}.'
      elif i in negative:
        store(i)
        return f'Aww, don\'t be {i}, you can talk to me to be less {i}.'  
      else:
        return store_vocab(i)
        
  
  if list[0] == 'i' and list[1] == 'am':
    if list[2] == 'feeling':
      list.remove(list[2])
      list.remove(list[1])
      list.remove(list[0])
      return understand_emotion(list)

# A repeat function so that there will always be a response between the User and the bot even if the bot doesn't know what to say.
def repeat(list):

  chance = ['yes', 'no']
  chance_picker = random.choice(chance)
  word_response = ['Sure !', 'Okay .', 'Right .', 'Yep .']

  Word_swap = [
    {'Word': 'me', 'Swap': 'you'},
    {'Word': 'my', 'Swap': 'your'},
    {'Word': 'i', 'Swap': 'you'},
              ]
  

  def swap_pronoun_2(list):
    for i in Word_swap:
      Word = i['Word']
      Swap = i['Swap']
      Obj = [{'Word': Word, 'Swap': Swap}]
      for elements in list:
        if elements == Word:         
          count = list.index(Word)
          list.remove(elements)
          list.insert(count, Swap)
  

  def mark_removal_2(list):
    Mark_removal = ['.', '?', '!']
    for i in list:
      for x in Mark_removal:
        if i in Mark_removal:
          list.remove(x)
  mark_removal_2(list)
  swap_pronoun_2(list)
  if chance_picker == 'yes':
    return " ".join(map(str,list)) + "?"
  else:
    return random.choice(word_response)

# A reminder function to remind the User about their emotions.
def remind():
  for item in data['people']:
    dictionary = item['dictionary']
    for category in dictionary:
      negative = category['negative']
  
  def remind_():
    for i in data['people']:
      emotion = i['emotion']
      for x in emotion:
        for i in negative:
          if x == i:
            print(f'Are you less {x} now ?')
            break
  remind_()
# A joke function that triggers if the text contains "Why" and will give the User nonsense response.
def joke(list):
  if "why" in list:
      return f"Because {random.choice(List_joke)}"


# A send function that allows the bot to send messages to the User.
def talk(res : str):
  count = 0
  list = res.split()
  randomfile = [greet(list), enter_name(list), question(list), emotion(list), joke(list)]
  ''' The for loop here loops all define functions until the perfect define function can handle a user's response or statement.
  If no define functions can handle a user's response then the bot doesn't know what to say. To maintain a natural conversation,
  the bot will return with a define function named "repeat"
  '''
  for i in randomfile:
    count += 1
    if i != None:
      return i
    elif count == 5:
      return repeat(list)
    '''
    Define functions needs to be in the same block as the json editor command in order to make changes to Storage.py
    '''
    with open(filename, 'w') as f:
      json.dump(data, f)