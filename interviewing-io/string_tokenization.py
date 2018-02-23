
# helper to find all words in set that are in string
input_string = "onecattwofourfourfourfour"
input_set = {"one", "cat", "two", "four, fo, ca, t, our, o, n, e"}
def helper_word_finder(input_set, input_str):
    all_words_in = []
    for word in input_set:
        if word in input_str:
            all_words_in.append(word)
    return all_words_in

all_words_in = helper_word_finder(input_set, input_string)

def can_make_string(all_words_in, input_str):
    first_letter_words = []
    if len(input_str) == 0:
        return True
    for word in all_words_in:
        if word[0] == input_str[0]:
            first_letter_words.append(word)
    for word in first_letter_words:
        all_words_in.remove(word)

    if len(first_letter_words) == 0:
        return False

    if len(first_letter_words) >= 2:
        updated_zero = input_str.replace(first_letter_words[0], "")
        updated_one = input_str.replace(first_letter_words[1], "")
        return can_make_string(all_words_in, updated_zero) or can_make_string(all_words_in, updated_one)
    elif len(first_letter_words) == 1:
        updated = input_str.replace(first_letter_words[0], "")
        return can_make_string(all_words_in, updated)


print can_make_string(all_words_in, input_string)
