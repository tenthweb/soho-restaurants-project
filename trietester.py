from trie import Trie

types = ['arcoxia 30', 'janumet','azilect', 'arcoxia 90', 'januvia', 'run', 'runners', 'runner', 'running','germane', 'ventolin']



type_tree = Trie()


type_tree.add_word_list(types)

print("What type of food would you like to eat?")





search_term = input("Type the beginning of that food type and press enter to see if it's here.\n")

search_results = type_tree.run_through_nodes_2(search_term)

if len(search_term) == 1:
    text_1 = "that"
    text_2 = "letter"

elif len(search_term) > 1:
    text_1 = "those"
    text_2 = "letters"
    
if search_results:

    elif len(search_results) == 1:
        
        text_3 = "only option is"
        
        print("With {0} beginning {1}, your {2} {3}. Do you want to look at {3} restuarants?".format(text_1, text_2, text_3, search_results[0]))

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
