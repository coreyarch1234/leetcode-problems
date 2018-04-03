# Insert comma after each word and the last word in list of words.

def comma(words):
    return [words[index] + ',' for index in range(len(words))]




words=['I', 'am', 'fabulous']
print comma(words)
