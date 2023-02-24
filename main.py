import random

# destination_list=['london', 'tokyo', 'portland']
# resturant_list = ['fish and chips', 'sushi', 'voodoo doughnuts']
# transportation_list = ['double decker' , 'shinkansen', 'uber']
# entertainment_list =['shipping ' , 'hot springs' ,  'music festival']


def print_greeting():
    print('Thank you for choosing the Day Trip Generator')
    print("-----------------------------------------------")
    print("We hope you enjoy your custom trip idea!") 
    print("-----------------------------------------------")

def pick_from_list(list_to_pick_from, topic):
    user_input = "N"
    while user_input != "Y":
        random_item= random.choice(list_to_pick_from)
        user_input = input (f'How about going to {random_item} for {topic}? Y/N')
        if user_input == "Y":return random_item
        


def run_trip_genarator():
    destination_list = ['london', 'tokyo', 'portland']
    resturant_list = ['fish and chips', 'sushi', 'voodoo doughnuts']
    transportation_list = ['double decker' , 'shinkansen', 'uber']
    entertainment_list =['shopping ' , 'hot springs' ,  'music festival']

    final_trip = {"destination": "", 
                "resturant": "", 
                "transportation": "", 
                "entertainment": ""}
    print_greeting()
    final_trip["destination"]=pick_from_list(destination_list, "destination")
    final_trip["resturant"]=pick_from_list(resturant_list, "resturant")
    final_trip["transportation"]=pick_from_list(transportation_list, "transportation")
    final_trip["entertainment"]=pick_from_list(entertainment_list, "entertainment")
    print(f'You are going to {final_trip["destination"]}\nYou will eat at {final_trip["resturant"]}\nTo get around the town use {final_trip["transportation"]}\nEnjoy the {final_trip["entertainment"]}')

run_trip_genarator()

