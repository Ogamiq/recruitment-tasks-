
hack = 'advantage'
letters = {'a':1,'d':2,'e':5,'g':2,'n':1,'t':4,'v':7}
phrases = {'ad':10,'ant':13,'age':24,'van':13,'tag':5}

def hack_calculator_extra(hack, letters, phrases):
    letters_counts = dict.fromkeys(letters.keys(),0)

    for letter in hack:
        if letter in letters_counts.keys():
            letters_counts[letter] += 1
        else:
            print("Letter {} in hack is not in the letters list".format(letter))


    phrases_counts = dict.fromkeys(phrases.keys(),0)

    for key in phrases_counts:
        phrases_counts[key] = hack.count(key)

    #test
    return phrases_counts


#test
phrases_counts = hack_calculator_extra(hack,letters,phrases)
for key in phrases_counts:
    print('{},{}'.format(key,phrases_counts[key]))

