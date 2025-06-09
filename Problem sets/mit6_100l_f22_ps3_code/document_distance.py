# 6.100A Fall 2022
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name:
# Collaborators:

# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.

import string
import math


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def text_to_list(input_text: str) -> list[str]:
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    whitespaces = string.whitespace
    text_copy = str(input_text)
    for char in whitespaces:
        text_copy = text_copy.replace(char, " ")
    while True:
        before = len(text_copy)
        text_copy = text_copy.replace("  ", " ")
        after = len(text_copy)
        if before == after:
            break
    return list(text_copy.replace(whitespaces," ").split(" "))


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable: str | list[str]) -> dict[str, int]:
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note: 
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """
    def check_keys(d: dict, element: str, value: int = 1) -> None:
        if element in d:
            d[element] += value
        else:
            d[element] = value
        
    dic = {}
    if isinstance(input_iterable, str):
        for char in input_iterable:
            check_keys(dic, char)
    else:
        for word in input_iterable:
            check_keys(dic, word)
    return dic


### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word: str) -> dict:
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    return get_frequencies(word)


### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1: dict[str,int], freq_dict2: dict[str,int]):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    if freq_dict1 == {} or freq_dict2 == {}:
        return 0
    union: set = set(freq_dict1.keys())
    union = union.union(freq_dict2.keys())
    denominator = 0
    numerator = 0
    for key in union:
        numerator += abs(freq_dict1.get(key, 0) - freq_dict2.get(key, 0))
        denominator += freq_dict1.get(key, 0) + freq_dict2.get(key, 0)
    

    similarity_score = 1 - numerator/denominator
    return round(similarity_score, 2)
### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    # print(f"freq_dict1: {freq_dict1}")
    # print(f"freq_dict2: {freq_dict2}")
    union: set = set(freq_dict1.keys())
    union = union.union(freq_dict2.keys())
    frequency = []
    for word in union:
        frequency.append([word, freq_dict1[word] + freq_dict2[word]])
    sorted_list = sorted(frequency, key= lambda x: x[1], reverse= True)
    word_list = []
    max_freq = sorted_list[0][1]
    for object in sorted_list:
        word = object[0]
        freq = object[1]
        if freq == max_freq:
            word_list.append(word)
    word_list.sort()
    return word_list
### Problem 5: Finding TF-IDF ###
def get_tf(file_path: str) -> dict[str, float]:
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    raw_string = load_file(file_path)
    word_list = text_to_list(raw_string)
    freq_dict = get_frequencies(word_list)
    words_total = 0
    for freq in freq_dict.values():
        words_total += freq
    tf_dict = {key: freq_dict[key]/words_total for key in freq_dict}
    return tf_dict

def get_idf(file_paths: list[str]) -> dict[str, float]:
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    list_of_words_list: list[list[str]] = []
    word_set = set()
    for file_path in file_paths:
        raw_string = load_file(file_path)
        words_list = text_to_list(raw_string)
        list_of_words_list.append(words_list)
        word_set = word_set | set(words_list)
    word_dic = {}
    for word in word_set:
        word_dic[word] = len(list(filter(lambda x: word in x, list_of_words_list)))
    total = len(file_paths)

    idf_dic = {}
    for word in word_dic:
        idf_dic[word] = math.log10(total / word_dic[word])
    return idf_dic


def get_tfidf(tf_file_path, idf_file_paths):
    """
        Args:
            tf_file_path: name of file in the form of a string (used to calculate TF)
            idf_file_paths: list of names of files, where each file name is a string
            (used to calculate IDF)
        Returns:
           a sorted list of tuples (in increasing TF-IDF score), where each tuple is
           of the form (word, TF-IDF). In case of words with the same TF-IDF, the
           words should be sorted in increasing alphabetical order.

        * TF-IDF(i) = TF(i) * IDF(i)
        """
    tf_dict: dict[str, float] = get_tf(tf_file_path)
    idf_dict: dict[str, float] = get_idf(idf_file_paths)
    words = set(tf_dict.keys())
    words_idf_list = []
    for word in words:
        if word not in idf_dict:
            raise ZeroDivisionError(f"the term {word} is not found in the collecton to calculate IDF. A division by zero error is invitable as no smoothing has been implemented. \n {idf_dict}")
        words_idf_list.append([tf_dict.get(word, 0)*idf_dict.get(word, 0), word])
    words_idf_list.sort()
    result = list(tuple(sublist[::-1]) for sublist in words_idf_list )
    return result


if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    ## Tests Problem 0: Prep Data
    # test_input = "hello  it is\nme\rmario"
    # expected = ["hello", "it", "is", "me", "mario"]
    # print(text_to_list(test_input))
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # print(world)      # should print ['hello', 'world', 'hello']
    # print(friend)     # should print ['hello', 'friends']

    ## Tests Problem 1: Get Frequencies
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    # print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    # # Tests Problem 2: Get Letter Frequencies
    # freq1 = get_letter_frequencies('hello')
    # freq2 = get_letter_frequencies('that')
    # print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    # print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    ## Tests Problem 3: Similarity
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # word1_freq = get_letter_frequencies('toes')
    # word2_freq = get_letter_frequencies('that')
    # word3_freq = get_frequencies('nah')
    # word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    # word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    # word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    # word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    # print(word_similarity1)       # should print 1.0
    # print(word_similarity2)       # should print 0.25
    # print(word_similarity3)       # should print 0.0
    # print(word_similarity4)       # should print 0.4

    ## Tests Problem 4: Most Frequent Word(s)
    # freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    # most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    # print(most_frequent)      # should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    # tf_text_file = 'tests/student_tests/hello_world.txt'
    # idf_text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    # tf = get_tf(tf_text_file)
    # idf = get_idf(idf_text_files)
    # tf_idf = get_tfidf(tf_text_file, idf_text_files)
    # print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    # print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    # print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]