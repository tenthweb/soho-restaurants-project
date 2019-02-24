from trie import Trie
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList


#Printing the Welcome Message
print_welcome()

#Write code to insert food types into a data structure here. The data is in data.py
type_trie = Trie()


type_trie.add_word_list(types)
    

#Write code to insert restaurant data into a data structure here. The data is in data.py


list_of_types = []
for restaurant in restaurant_data:
    if restaurant[0] not in list_of_types:
        list_of_types.append(restaurant[0])

def print_restaurant_info(type):
    print("\nThe {0} restaurants in Soho are...".format(type))
    print("\n---------------------------\n")
    current_node = finder.retrieve(type)  
    while current_node.get_next_node():
        print_restaurant(current_node.value)
        print("\n---------------------------\n")
        current_node = current_node.get_next_node() 


finder = HashMap(len(list_of_types))

def map_types_to_restaurants(restaurant_type):
      restaurant_ll = LinkedList()
      for restaurant in restaurant_data:
          if restaurant[0] == restaurant_type:
              restaurant_ll.insert_beginning(restaurant)

      finder.assign(restaurant_type, restaurant_ll.get_head_node())




for restaurant_type in list_of_types:
    map_types_to_restaurants(restaurant_type)


      
#Write code for user interaction here
while True:

    print("\nWhat type of food would you like to eat?")
    search_term = str(input("Type the beginning of that food type and press enter to see if it's here.\n")).lower()
 

    #Search for user_input in food types data structure here
    search_results = type_trie.run_through_nodes_2(search_term)

    if len(search_term) == 1:
        text_1 = "that"
        text_2 = "letter"

    elif len(search_term) > 1:
        text_1 = "those"
        text_2 = "letters"
        
    if search_results:

        if len(search_results) == 1:
            
            text_3 = "only choice is"
            
            choice = str(input("With {0} beginning {1}, your {2} {3}. Do you want to look at {3} restaurants? Enter y for yes and n for no. ".format(text_1, text_2, text_3, search_results[0]))).lower()
            break

            

        elif len(search_results) == 2:
            
            text_3 = "choices are"
            
            print("With {0} beginning {1}, your {2} {3} and {4}.".format(text_1, text_2, text_3, search_results[0], search_results[1])) 
        
        else:
            
            text_3 = "choices are"
            
            print("With {0} beginning {1}, your {2} ".format(text_1, text_2, text_3), end='')

            for word_index in range(len(search_results) -1): 
                print(search_results[word_index] + ", ", end='')
        
            print('and ' + search_results[-1] + ".")
    else:
        print("Sorry, I don't know any food types in the area that start with those letters. Please try again.")


    #After finding food type write code for retrieving restaurant data here



def print_restaurant(restaurant):
    print("Name: " + restaurant[1])
    print("Price: " + restaurant[2])
    print("Rating: " + restaurant[3])
    print("Address: " + restaurant[4])
    

if choice == 'y':
    print_restaurant_info(search_results[0])   
    






    
    
      
    
  

  




