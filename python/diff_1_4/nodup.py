
def word_count_dict(parag_list):
    ''' Takes in a list of lists and counts evey word, returns a dictionary'''
    dict_counter = {}
    for word in parag_list:
        dict_counter[word] = dict_counter.get(word, 0) + 1  # if item does not exist add it, if it does exist add 1 to the value
        if dict_counter[word] >= 2:
            return "no"
    return "yes"  # returns a dict with the word as a key and the count as value


inp = input()
inp_list = inp.split()
print(word_count_dict(inp_list))