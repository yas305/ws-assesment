import math


def get_transposed_gridstring(grid, row_length) -> tuple:
    """":returns a tuple of the transposed grid as a string and a list"""
    list = []

    # split the grid into a list of rows ever ROW_LENGTH characters
    for i in range(0, row_length):
        list.append(grid[i::row_length])
    # return the list as a single string and as a list
    return (("".join(list)), list)


class WordSearch:
    dict = {}
    grid_length = 0
    row_length = 0
    default_grid_first = []
    transposed_grid_first = []
    MAX_WORD_LENGTH = 24

    def __init__(self, grid):

        self.grid = self.clean_string(grid)
        self.grid_length = len(grid)
        self.row_length = int(math.sqrt(self.grid_length))
        self.default_grid_first = self.seperate_words()
        print(self.default_grid_first)
        self.transposed_grid_first = get_transposed_gridstring(grid, self.row_length)[-1]
        print(self.transposed_grid_first)
        self.dict = self.getallsubstring(self.default_grid_first + self.transposed_grid_first)

    def clean_string(self, grid_string) -> str:
        """removes all non-alphanumeric characters from a word"""
        regex = "/^[A-Z]+"

        # remove all non alphanumeric characters and whitespace
        grid_string = grid_string.replace(regex, "").replace(" ", "")

        if len(grid_string) % math.sqrt(len(grid_string)) != 0:
            while len(grid_string) % math.sqrt(len(grid_string)) != 0:
                grid_string = grid_string[:-1]
        return grid_string

    def seperate_words(self) -> list:

        """"seperates one massive string into into a list words of length GRID_ROW_LENGTH"""

        seperated_words = []
        # split the string every row_length characters
        for i in range(0, self.grid_length, self.row_length):
            seperated_words.append(self.grid[i:i + self.row_length])
        # print(seperated_words)
        return seperated_words

    def getallsubstring(self, word_list) -> {}:
        """returns a dictionary of all possible substrings upto a maximum length MAX_WORD_LENGTH (24 in this case)"""
        dict = {}

        for word in word_list:
            for i in range(len(word)):
                for x in range(i, len(word) + 1):
                    # only add the substring if it is not already in the dictionary and the length is greater than 1
                    # and less than the max word length
                    if word[i:x] not in dict and 1 < len(word[i:x]) <= self.MAX_WORD_LENGTH:
                        dict[word[i:x]] = True
        return dict

    def is_present(self, word) -> bool:
        if type(self.dict.get(word)) == bool:
            return True
        else:
            return False

    # def is_present2(self, word) -> bool:
    #     # check if word is in grid
    #     if word in self.default_grid_first or word in self.transposed_grid_first:
    #         # get the index of the word in the grid
    #         first_index = self.default_grid_first.index(word)
    #         last_index = first_index + len(word)
    #         print(first_index)
    #         print(last_index)
    #         # check if the indexes are within the grid the bounds of grid length
    #         if first_index >= 0 and last_index <= self.grid_length:
    #             return True
    #         return False

    # def is_present_using_in(self, word):
    #     #loop through separated words
    #     for i in self.default_grid_first:
    #         if word in i:
    #             return True
    # for i in self.transposed_grid_first:
    #     if word in self.transposed_grid_first[i]:
    #         return True
    # return False
