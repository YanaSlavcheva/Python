word = input('Enter first text: ')
separator = input('Enter second text: ')

if separator in word:

    # with arithmetics

    # start_index_for_cut = word.index(separator) + len(separator)
    # result = (word[start_index_for_cut:]).lstrip()


    # no arithmetics

    # result = word.partition(separator)[2].lstrip()


    # no arithmetics 2

    result = (word.split(separator, 1))[-1].lstrip()

else:
    result = word

print(result)
