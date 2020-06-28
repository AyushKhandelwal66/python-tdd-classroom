import re
class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        return input_str[::-1]

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        if(character=='A' or character=='a' or character=='E' or
           character =='e' or character=='I'or character=='i' or
           character=='O' or character=='o' or character=='U' or character=='u'):
            return True
        else:
            return False

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        word=re.findall(r"\w+",sentence) #store all the string into a list
        n=max(word,key=lambda x: len(x))
        return n
    
        
    def get_word_lengths(self, text):
        return [len(x) for x in text.split()]
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
          
      
