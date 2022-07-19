import sys


def word_split(str_arr):
    """ 
        Splits a possible compound word into 2 existing words in a set of words
        Inputs: str_arr -> first arg (compound word: string) second arg (csv of existing words: string)
        Output: csv splitted word or not possible splitted word combination message
    """
    words = str_arr[1].split(",")
    # word dictionary to access possible words in O(1) time
    word_dict = dict(zip(words, words))

    possible_word = ""
    compound_word = str_arr[0]
    # index to split onto two possible words
    for index, char in enumerate(compound_word):
        possible_word += char
        try:
            # check if the left side of the word exists as well as the right side
            if word_dict[possible_word] and word_dict[compound_word[index + 1:]]:
                # return if true
                return f"{possible_word},{compound_word[index + 1:]}"
        except KeyError:
            # handle KeyError in this case continue
            continue

    return "The string is not possible"

if __name__ == "__main__":
    string = sys.argv[1]
    string_array = sys.argv[2]
    print(word_split([string, string_array]))
