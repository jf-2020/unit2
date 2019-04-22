# into_to_apis_.py - this prgm works along with the DC day 6's API exercise
#
# jf - 4/22


###########


# import the list of characters, which is, essentially, a json object
# that can be treated as a list of dicts
from characters import characters

# also, import the houses
from houses import houses as HOUSES

from pprint import pprint


###########


# count the number of names starting with "A" & "Z"
number_of_names_A, number_of_names_B = 0, 0

# count the number of characters that're dead
number_dead = 0

# count the number of Valyrian
number_valyrian = 0

# max val for chars and number of titles
max_chars_and_titles = 0
max_character = ''

# store name for actor that plays "Hot Pie"
hot_pie_actor = ''

# store number of characters not in the tv show
number_characters_not_in_show = 0

# keep track of those characters with the last name 'Targaryen'
targaryen_characters = list()

# build a list of the respective houses
houses = list()
for h in HOUSES:
    if HOUSES[h] not in houses:
        houses.append(HOUSES[h])

# and a list of correspondent house counts
house_counts = [0 for _ in range(len(houses))]


###########


# loop over the characters
for character in characters:
    
    # check it begins with an "A", upper or lower
    if character['name'][0] == 'A' or character['name'][0] == 'a':
        
        # if so, bump up the count
        number_of_names_A += 1

    # check if it begins with a "Z", upper or lower
    elif character['name'][0] == 'Z' or character['name'][0] == 'z':

        # if so, bump up the count
        number_of_names_B += 1

    # check if the character is dead
    elif character['died'] != "":

        # if so, bump up the count
        number_dead += 1

    # count the number of Valyrians
    elif character['culture'] == 'Valyrian':

        # if so, bump up the count
        number_valyrian += 1

    # check if char's number of titles is greater than current max
    elif len(character['titles']) > max_chars_and_titles:

        # if so, update the max & max character
        max_chars_and_titles = len(character['titles'])        
        max_character = character['name']

    # find "Hot Pie" actor
    elif character['name'] == 'Hot Pie':

        # update the actor
        hot_pie_actor = character['playedBy'][0]

    # check whether or not the 'tvSeries' attribute is empty (i.e. the character
    # is not in the tv show)
    elif len(character['tvSeries']) == 0:

        # if so, bump up the count
        number_characters_not_in_show += 1

    # check if the character's last name is 'Targaryen'
    elif character['name'] and 'Targaryen' in character['name']:

        # if so, add the character to the appropriate list
        targaryen_characters.append(character['name'])

    # keep count of the allegiances to each house
    for house_url in character['allegiances']:

        # get the house
        house = HOUSES[house_url]

        # get the correct house index
        get_house_index = houses.index(house)

        # update the corresponding house count
        house_counts[get_house_index] += 1


###########


# print out the relevant counts
print("Number of characters whose names begin with 'A':", number_of_names_A)
print("Number of characters whose names begin with 'Z':", number_of_names_B)
print("Number of characters that're dead:", number_dead)
print("Number of characters that're Valyrian:", number_valyrian)
print("The character with the most titles is", max_character, "and has %d titles" % max_chars_and_titles)
print("The actor who plays 'Hot Pie' is:", hot_pie_actor)
print("Number of characters not in the TV show:", number_characters_not_in_show)
print("Characters whose last name is Targaryen:", targaryen_characters)

print()

# build the histogram of houses
fstring = "{:35} | {}"

for index, house in enumerate(houses):
    print(fstring.format(' '.join(house.split()[1:]), 'x'*house_counts[index]))