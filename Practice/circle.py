words  = "x"

letter_list = []
for y in range(30,-30, -1):
    list_X  = []
    letters = ''
    for x in range(-30,30,1):
        if (x**2 + y**2) <= 400:
            letters += words
        else:
            letters += " "
    list_X.append(letters)
    letter_list += list_X
print('\n'.join(letter_list))
