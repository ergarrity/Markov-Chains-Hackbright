"""Generate Markov text from text files."""

#from random import choice
import random, sys
from string import punctuation # import string with punctuation

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    #text=str(open(file_path)).strip("\n")
    #text = open(file_path).read()
    #print(text)
    # your code goes here

    return  open(file_path).read() #opens and reads the file and outputs it


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    chains = {} #initilize empty dictionary


    list_of_words = text_string.split() #makes list of words from the inputted string of text

    for i in range(len(list_of_words)-2): #iterates through that list of words, stopping slightly before end to avoid out-of-range
        bigram = (list_of_words[i], list_of_words[i+1]) #makes a bigram with the current item and the next
        if bigram not in chains: #checks if the bigram is already a key in the chains dictionary
            chains[bigram]=[] #adds it to the dictionary with an empty list of a value, this allows us to add many next-possible-words as we go through
        chains[bigram].append(list_of_words[i+2])#appends the following word to the list of possible following words associated with that bigram

    return chains

def make_chains_n(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    chains = {} #initilize empty dictionary


    list_of_words = text_string.split() #makes list of words from the inputted string of text

    for i in range(len(list_of_words)-n): #iterates through that list of words, stopping n before end to avoid out-of-range
        ngram_list=[]
        for j in range(n):
            ngram_list.append(list_of_words[i+j])
        ngram = tuple(ngram_list)
        if ngram not in chains: #checks if the bigram is already a key in the chains dictionary
            chains[ngram]=[] #adds it to the dictionary with an empty list of a value, this allows us to add many next-possible-words as we go through
        chains[ngram].append(list_of_words[i+n])#appends the following word to the list of possible following words associated with that n-gram
    #for item in chains:
     #   print(item, chains[item])
    return chains


def make_text(chains):
    """Return text from chains."""
    first_bigram=random.choice(list(chains.keys())) #select a random key from our dictionary to use as our initial bigram

    words = [] #this empty list will eventually be filled with our generated text!

    words.append(first_bigram[0]) #appends the first item of initial bigram
    words.append(first_bigram[1]) #appends the second part of the initial bigram

    next_bigram = first_bigram #sets up a "next_bigram"
    while True: #this loops until it breaks
        try: #this checks for a key error 
            next_word = random.choice(chains[next_bigram]) #chooses a 
            words.append(next_word)
            #print(next_word)
            next_bigram=(next_bigram[1], next_word)
            pass
        except KeyError:
            break
    #add next word randomly from values
    #make new bigram with added word
    #loop using new bigram as start

    # your code goes here

    return " ".join(words)

def make_text_n(chains):
    """Return text from chains."""
    first_ngram=(random.choice(list(chains.keys()))) #select a random key from our dictionary to use as our initial bigram
    while not first_ngram[0][0].isupper():
        first_ngram=random.choice(list(chains.keys())) 

    words = [] #this empty list will eventually be filled with our generated text!

    for i in range(len(first_ngram)):
        words.append(first_ngram[i])

    # alternative to for loop on line above
    # words = list(first_ngram)



    
    next_ngram = first_ngram #sets up a "next_bigram"
    while True: #this loops until it breaks
        try: #this checks for a key error 
            next_word = random.choice(chains[next_ngram]) #
            words.append(next_word)
            #print(next_word[-1] in punctuation, next_word[-1])
            if next_word[-1] in punctuation:
               # print("TEST")
                words.append("\n")
            #print(next_word)
            next_ngram_list=list(next_ngram)
            next_ngram_list.append(next_word)

            #print ("NEXT", next_ngram_list)
            next_ngram=tuple(next_ngram_list[1:])
            pass
        except KeyError:
            if not next_ngram[-1][-1] in punctuation:
                next_ngram = (random.choice(list(chains.keys())))
            break
    #add next word randomly from values
    #make new bigram with added word
    #loop using new bigram as start

    # your code goes here

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
# Get a Markov chain
chains = make_chains_n(input_text, int(sys.argv[2]))
## Produce random text
random_text = make_text_n(chains)

print(random_text)
