from trienode import TrieNode

class Trie:

    def __init__(self):
        self.root = TrieNode('')

    def add_word(self, word):

        # deal with invalid input
        if not word:
            pass


        else:

            #set current node at root of trie

            current_node = self.root

            # loop through letters in word
            for letter in word:

                # deal with case where letter does not yet exist at this level


                repeated_letter_count = current_node.repeated_letter


                if letter not in current_node.children:

                    # case where two consecutive letters are the same
                    if letter == current_node.letter:
                        repeated_letter_count += 1


                    # create new node
                    current_node.children[letter] = TrieNode(letter, repeated_letter_count)


                # deal with case where letter already exists at this level

                current_node = current_node.children[letter]

            #after last letter, mark end of word
            current_node.word_end = True


    
    def travel(self):
        current_node = self.root
        while current_node.children:
            print(current_node.children.keys())
            choice = input("Which letter would you like to follow? ")
            if choice in current_node.children.keys():
                current_node = current_node.children[choice]
            else:
                print("Sorry, try another letter!")

        print("end of word!")


    def search(self, term):

        if len(term) == 0:
            print("Search error. Blank search term.")
            return False
            

        if term[0] in self.root.children:

            # start off with at the node beneath the root whose letter is
            # the first letter in "term" 

            current_node = self.root.children[term[0]]

            # Iterate through the indices of each letter in term and try to
            # match them with nodes and travel along a branch

            for letter_index in range(len(term)):

                # If we get matches all along the branch, we hit the last
                # letter of our term. If the last letter of our term is the
                # end of a word in our tree, we have found a match for our
                # term!

            

                if letter_index == len(term) - 1 and current_node.word_end == True:
                    return True
                
                

                    # If we get a match between the nth letter of our term and the letter in the
                    # (n + 1)th node in our tree, but we haven't reached the end of our term,
                    # we keep going, and check if the next letter has a match in the current node's
                    # chuldren
                     
                if current_node.letter == term[letter_index]:
                    
                    if letter_index < len(term) - 1:
                        
                        if term[letter_index + 1] in current_node.children:
                            current_node = current_node.children[term[letter_index + 1]]
                            
                        else:
                            return False
                    else:
                        return False
                else:
                   return False
            
        return False


    def delete_word(self, word):
        
            word_exists = self.search(word)
##
##        if not word_exists:
##            print("Error! Word not in dictionary!")
##        else:



            if word[0] in self.root.children:
                current_node = self.root.children[word[0]]
                last_fork = None
                count_1 = 0



                # find point where word-branch diverges from the main branch
                # let's call these "forks", and count words that end in the middle of a tree as forks
                # eg. the the first "n" in the branch "runner" is counted as a fork if "run" is also in our list

                for letter_index in range(len(word) -1):
                    if len(current_node.children) > 1 or current_node.word_end:
                        last_fork = current_node.letter
                        count_1 +=1
        
                    
                    current_node = current_node.children[word[letter_index + 1]]



                # if there's no branching in the tree, it's just a line, so cut it off at the root.

                if count_1 == 0:
                    first_letter = self.root.children
                    self.root.children.pop(word[0])

                else:       
                        
                    # go back to lowest fork and delete the node in 'word' after that point

                    count_2 = 0

                    current_node = self.root.children[word[0]]
                    for letter_index in range(len(word) -1):
                        


                        if len(current_node.children) > 1 or current_node.word_end:
                            count_2 +=1


                        if current_node.letter == last_fork and count_2 == count_1:
                            current_node.children.pop(word[letter_index +1])

                            break
                         
                        # if we reach a fork, increment our fork count for this branch



                        else:
                            if current_node.children:
                                current_node = current_node.children[word[letter_index + 1]]


                        # if we reach the last fork, delete the node corresponding to the next letter in the word
                                       
                            





 #   def iterate(self):
        





    def travel_2(self):
        word = ''
        current_node = self.root
        while current_node.children:
            for child in current_node.children:
                word += child
                current_node = current_node.children[child]
                
                break
        return word

    def run_through_nodes(self):

        list_of_words = []

        while self.root.children:
            list_of_words.append(self.travel_2())
            self.delete_word(list_of_words[-1])
        
        self.add_word_list(list_of_words)
        return list_of_words


    def travel_based_on_prefix(self, prefix):
        suffix = ''
        current_node = self.root

        
        for letter in prefix:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                return

        while current_node.children:
            for child in current_node.children:
                suffix += child
                current_node = current_node.children[child]
                
                break

        return suffix

    def run_through_nodes_2(self, prefix):

        list_of_words = []
        top_node = self.root

        if self.search(prefix):
            print(prefix)
            list_of_words.append(prefix)
        
        for letter in prefix:
            if letter in top_node.children:
                top_node = top_node.children[letter]

        


        while top_node.children:
            
            suffix = self.travel_based_on_prefix(prefix)
            if prefix and suffix:
                word = prefix + suffix
            else:
                break

            list_of_words.append(word)
            
            
            self.delete_word(word)
            
        
        self.add_word_list(list_of_words)

        return list_of_words




        

##    def get_all_words(self)
##    current_node = self.root:
##        word_list = []
##        nodes_to_check
##        while nodes_to_check:
##            

##    def copy_tree(self):
##        current_old_node = self.root
##        current_new_node = current_old_node
##        
##        else:
##            current_node = self.root
            
        
        

##    def get_suffixes(self, term):
##
##        current_node = self.root.children[term[0]]
##
##        for letter_index in range(len(term)):
##
##
##            if letter_index == len(term) - 1:
##                print("The words starting with those letters are \n" + term,end ='' )
##                for key in current_node.children:
##        
##                    print(self.run_through_nodes(current_node, key), end='')
##                
##            else:
##                    if current_node.letter == term[letter_index]:
##                        if term[letter_index + 1]:
##                            if term[letter_index + 1] in current_node.children:
##                                current_node = current_node.children[term[letter_index + 1]]
            

            
    def add_word_list(self, word_list):
        for word in word_list:

            self.add_word(word)

