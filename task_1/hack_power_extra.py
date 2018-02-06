hack = 'advantage'
letters = {'a':1,'d':2,'e':5,'g':2,'n':1,'t':4,'v':7}
phrases = {'ad':10,'ant':13,'age':24,'van':13,'tag':5}

def hack_calculator_extra(hack, letters, phrases):
    #returns a value of a hack based on a dynamically provided dictionaries
    #of letters and it's values and of phrases and it's values
    #first by counting number of occurrences of each letter and phrase and assigning them to the dictionaries
    #than by using those counts and values for letters and phrases to compute and return the final result.

    letters_counts = dict.fromkeys(letters.keys(),0)
    for letter in hack:
        if letter in letters_counts.keys():
            letters_counts[letter] += 1

    phrases_counts = dict.fromkeys(phrases.keys(),0)
    for key in phrases_counts:
        phrases_counts[key] = hack.count(key)

    letters_score = 0
    for key in letters:
        letters_score += letters[key]*sum(range(letters_counts[key]+1))

    phrases_score = 0
    for key in phrases:
        phrases_score += phrases[key]*phrases_counts[key]

    return letters_score + phrases_score


print(hack_calculator_extra(hack,letters,phrases))