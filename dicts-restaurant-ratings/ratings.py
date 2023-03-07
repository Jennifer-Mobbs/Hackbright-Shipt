"""Restaurant rating lister."""


new_file = open("scores.txt")
dict_scores = {}
#loop that pulls the text in
for line in new_file:
    line = line.rstrip()
    rating = line.split(":")
    
    # this loop adds the arrays to a dictionary
    for item in range (0, len(rating)):
       dict_scores[rating[0]] = rating[1] 
# for key_names in sorted(dict_scores.items()):
    # print(f'{key_names[0]} is rated at {key_names[1]}.')

rest_name = input("What's the name of the restuarant:").title()

rest_rating = input("What rating would you give this restaurant:")
dict_scores[rest_name] = rest_rating

for key_names in sorted(dict_scores.items()):
    print(f'{key_names[0]} is rated at {key_names[1]}.')

        

