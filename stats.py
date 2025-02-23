def num_of_words(text):
    with open(text) as f:
        num = f.read()
    return len(num.split())

def character(text):
    char_dict = {}
    with open(text) as f:
        contents = f.read()
        for t in contents:
            lower_case = t.lower()
            if lower_case.isalpha():
                if lower_case in char_dict: #filter non letters
                    char_dict[lower_case] += 1
                else:
                    char_dict[lower_case] = 1
    return char_dict

def sorted_characters(dict):
    return sorted(dict.items(), reverse=True, key=lambda item: item[1]) 