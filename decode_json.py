# take dictionary and convert to json string representation

def decode_json(dictionary):
    open_bracket  = "{"
    close_bracket = "}"

    output_json = ""
    for key, value in dictionary.items():
        if type(value) is dict:
            output_json += key  + ":" + decode_json(value) + " "
        else:
            output_json += (key + ":" + value) + " "

    #add commas
    for index in range(len(output_json) - 1):
        if output_json[index] == " ":
            if output_json[index + 1] != "}":
                output_json = output_json[0:index] + "," + output_json[index + 1:]
    return open_bracket + output_json + close_bracket



print decode_json({"a": "apple", "b": {"b": "blueberry", "c": "cranberry"}, "c": {"c": "capjuice", "d": "dingleberry", "e": {"f": "fact", "p": "plum"} }})
# should return "{"a": "apple", "b": {"b": "blueberry", "c": "cranberry"}}"
print
print decode_json({"a": "apple", "b": "blueberry"})
