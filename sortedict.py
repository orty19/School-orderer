letters = 'abcdefghijklmnop'.upper()
newdict = {}
def sort(dict):
    global newdict
    print(dict)
    for letter in letters:
        for key in dict:
            #print(f'{key}.startswith({letter}): {key.startswith(letter)}')
            if key.startswith(letter):
                newdict[str(key)] = dict[key]
