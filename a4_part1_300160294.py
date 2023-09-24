#Family name: Sebastian Doka
#Student number: 300160294
#Course : ITI 1120
#Assignment Number 4 Part 1
#date: 2020 11 02

def is_valid_file_name():
    '''()->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name
import re
def clean_word(word):
    '''(str)->str
    Returns a new string which is lowercase version of the given word
    with special characters and digits removed

    The returned word should not have any of the following characters:
    ! . ? : , ' " - _ \ ( ) [ ] { } % 0 1 2 3 4 5 6 7 8 9 tab character and new-line character

    >>> clean_word("co-operate.")
    'cooperate'
    >>> clean_word("Anti-viral drug remdesivir has little to no effect on Covid patients' chances of survival, a study from the World Health Organization (WHO) has found.")
    'antiviral drug remdesivir has little to no effect on covid patients chances of survival a study from the world health organization who has found'
    >>> clean_word("1982")
    ''
    >>> clean_word("born_y1982_m08\n")
    'bornym'

    '''
    string=word.lower()
    bad_char='''!!.?:,'"-_\()[]{}%0123456789\n\t'''
    for i in bad_char:
        string=string.replace(i, '')

    return str(string)
    pass


def test_letters(w1, w2):
    '''(str,str)->bool
    Given two strings w1 and w2 representing two words,
    the function returns True if w1 and w2 have exactlly the same letters,
    and False otherwise

    >>> test_letters("listen", "enlist")
    True
    >>> test_letters("eekn", "knee")
    True
    >>> test_letters("teen", "need")
    False
    '''

    length=len(w1)
    length2=len(w2)
    sort=sorted(w1)
    sort2=sorted(w2)
    if length==length2 and sort==sort2:
        return True
    else:
        return False
    
def create_clean_sorted_nodupicates_list(s):
    '''(str)->list of str
    Given a string s representing a text, the function returns the list of words with the following properties:
    - each word in the list is cleaned-up (no special characters nor numbers)
    - there are no duplicated words in the list, and
    - the list is sorted lexicographicaly (you can use python's .sort() list method or sorted() function.)

    This function must call clean_word function.

    You may find it helpful to first call s.split() to get a list version of s split on white space.
    
    >>> create_clean_sorted_nodupicates_list('able "acre bale beyond" binary boat brainy care cat cater crate lawn\nlist race react cat sheet silt slit trace boat cat crate.\n')
    ['able', 'acre', 'bale', 'beyond', 'binary', 'boat', 'brainy', 'care', 'cat', 'cater', 'crate', 'lawn', 'list', 'race', 'react', 'sheet', 'silt', 'slit', 'trace']

    >>> create_clean_sorted_nodupicates_list('Across Europe, infection rates are rising, with Russia reporting a record 14,321 daily cases on Wednesday and a further 239 deaths.')
    ['', 'a', 'across', 'and', 'are', 'cases', 'daily', 'deaths', 'europe', 'further', 'infection', 'on', 'rates', 'record', 'reporting', 'rising', 'russia', 'wednesday', 'with']
    '''
    clean=clean_word(s)
    cleanList=clean.split(' ')

    for i in cleanList:

        if cleanList.count(i) > 1:
            
            cleanList.remove(i)

    sort=sorted(cleanList)

    return sort

def word_anagrams(word, wordbook):
    '''(str, list of str) -> list of str
    - a string (representing a word)
    - wordbook is a list of words (with no words duplicated)

    This function should call test_letters function.

    The function returs a (lexicographicaly sorted) list of anagrams of the given word in wordbook
    >>> word_anagrams("listen", wordbook)
    ['enlist', 'silent', 'tinsel']
    >>> word_anagrams("race", wordbook)
    ['acre', 'care']
    >>> word_anagrams("care", wordbook)
    ['acre', 'race']
    >>> word_anagrams("year", wordbook)
    []
    >>> word_anagrams("ear", wordbook)
    ['are', 'era']
    '''
    anagram_list= []

    for i in wordbook:

        if test_letters(word, i)== True and word != i:
            anagram_list.append(i)

        

        
    return anagram_list

def count_anagrams(l, wordbook):
    '''(list of str, list of str) -> list of int

    - l is a list of words (with no words duplicated)
    - wordbook is another list of words (with no words duplicated)

    The function returns a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.
    
    Whenever a word in l is the same as a word in wordbook, that is not counted.

    >>> count_anagrams(["listen","care", "item", "year", "race", "ear"], wordbook)
    [3, 2, 3, 0, 2, 2]

    The above means that "listen" has 3 anagrams in wordbook, that "care" has 2 anagrams in wordbook ...
    Note that wordbook has "care", "race" and "acre" which are all anagrams of each other.
    When we count anagrams of "care" we count "race" and "acre" but not "care" itself.
    '''

    counted= []

    for i in l:

        list=word_anagrams(i,wordbook)
        counted.append(len(list))

    return counted



def k_anagram(l, anagcount, k):
    '''(list of str, list of int, int) -> list of str

    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a  (lexicographicaly sorted) list of all the words
    in l that have exactlly k anagrams (in wordbook as recorded in anagcount)

    k_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2], 2)
    ['care', 'ear', 'race']
    '''
    k_list= []

    for i in range(len(anagcount)):

        if anagcount[i]==k:
            k_list.append(l[i])

    kList=sorted(k_list)

    return kList
            

def max_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with maximum number of anagrams (in wordbook as recorded in anagcount)
    
    >>> max_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['item', 'listen']
    '''
    max_list= []

    for i in range(len(anagcount)):

        if anagcount[i]==max(anagcount):
            max_list.append(l[i])

    maxList=sorted(max_list)

    return maxList
            
   

def zero_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with no anagrams
    (in wordbook as recorded in anagcount)
    
    >>> zero_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['year']
    '''

    empty_list= []

    for i in range(len(anagcount)):

        if anagcount[i]==0:
            empty_list.append(l[i])

    sortList=sorted(empty_list)

    return sortList
            

            



                
    
##############################
# main
##############################


wordbook=open("english_wordbook.txt").read().lower().split()
list(set(wordbook)).sort()

print("Would you like to:")
print("1. Analize anagrams in a text -- given in a file")
print("2. Get small help for Scrabble game")
print("Enter any character other than 1 or 2 to exit: ")
choice=input()

if choice=='1':
    file_name=get_file_name()
    rawtx = open(file_name).read()
    l=create_clean_sorted_nodupicates_list(rawtx)
    anagcount = count_anagrams(l,wordbook)

    print("\nOf all the words in your file, the following words have the most anagrams:")
    maxList=max_anagram(l, anagcount)
    print(maxList)

    print("Here are their anagrams: ")
    for i in range(0,len(maxList)):

       
        word=maxList[i]
        print("Anagrams of " + maxList[i] + " are:")
        print(word_anagrams(word,wordbook))

       

    print("Here are the words that have no anagrams:\n")
    print(zero_anagram(l,anagcount))

    print("Say you are interested if there is a word in your file that has exactly k anagrams")
    k=int(input("Enter a number for variable k: "))
    print("Here are the word(s) in your file that have " + str(k) + " anagrams: ")
    print(k_anagram(l,anagcount, k))

    pass
    
elif choice=='2':
    space=True
    while space:
        
        letters=str(input("Enter the letters that you have, one after another with no space: "))
        
        if (' ' in letters)==True:
            
            print("Error: You entered space(s).")
            space=True
            
        else:
            
            space=False
            correct=True
            
            while correct:
                question=int(input("Would you like help forming a word with\n1. all these letters\n2.all but one of these letters?\n"))
                if question==1:
                    if len(word_anagrams(letters,wordbook))==0:
                        print("There is no word comprised of exactly these letters.")
                        pass
                    else:
                        print("Here are the words that are comprised of exacty these letters:")
                        print(word_anagrams(letters,wordbook))
                        
                
                    correct=False
                    
                elif question==2:
                    print("The letters you gave us are: " + letters)
                    print("Let's see what we can get if we ommit one of these letters.")
                    sub= []
                    for i in range(0,len(letters)):
                        sub= letters[:i] + letters[i+1:]
                        print("Without the letter in position " + str(i+1) + " we have letters " + sub)

                        if len(word_anagrams(sub,wordbook))==0:
                            print("There is no word comprised of exactly these letters.")
                            pass
                        else:
                            print("Here are the words that are comprised of exacty these letters:")
                            print(word_anagrams(sub,wordbook))
                        
                    correct=False
                    
                else:
                    
                    print("Only 1 or 2 accepted.Please try again")
                    correct=True
                    
                    

                
    
    pass
                       
                      
else:
    print("Good bye")


