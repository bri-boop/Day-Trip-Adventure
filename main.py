import random

destination_list=['london', 'tokyo', 'portland']
resturant_list = ['fish and chips', 'sushi', 'voodoo doughnuts']
transportation_list = ['double decker' , 'shinkansen', 'uber']
entertainment_list =['shipping ' , 'hot springs' ,  'music festival']


def print_greeting():
    print('Thank you for choosing the Day Trip Generator')
    print("-----------------------------------------------")
    print("We hope you enjoy your custom trip idea!")
    print("-----------------------------------------------")

def pick_from_list(list_to_pick_from, topic):
    random_item= random.choice(list_to_pick_from)
    user_input = input (f'How about going to {random_item} for {topic}? Y/N')
    while user_input != "Y":
        random_item = random.choice(list_to_pick_from)
        user_input = input (f'How about eating {random_item} for {topic}? Y/N')
    return random_item
    while user_input:"Y":print ("Great! Onto food!")

def run_trip_genarator():
    destination_list = ['london', 'tokyo', 'portland']
    resturant_list = ['fish and chips', 'sushi', 'voodoo doughnuts']
    transportation_list = ['double decker' , 'shinkansen', 'uber']
    entertainment_list =['shipping ' , 'hot springs' ,  'music festival']

final_trip = {"destination": "", 
              "resturant": "", 
              "transportation": "", 
              "entertainment": ""}
print_greeting()
final_trip["destination"]=pick_from_list(destination_list, "destination")
print(final_trip['destination'])
final_trip["resturant"]=pick_from_list(resturant_list, "resturant")
