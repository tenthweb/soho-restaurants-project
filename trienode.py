class TrieNode:
  def __init__(self, letter, repeated_letter=0):
        self.letter = letter
        self.children = {}
        self.word_end = False
        self.repeated_letter = repeated_letter
  
