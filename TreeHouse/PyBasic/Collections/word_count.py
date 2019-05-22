def word_count(some_string):
    all_words = some_string.split()
    dictionary = {}
    for word in all_words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary

print(word_count("I do not like it Sam I Am"))
