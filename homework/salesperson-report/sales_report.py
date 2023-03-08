"""Generate sales report showing total melons each salesperson sold."""

#two lists are created
salespeople = []
melons_sold = []
# the file sales-report is opened 
f = open('sales-report.txt')
#the for loop iterating over each line of text in the file f
for line in f:
    #each line has the white space removed
    line = line.rstrip()
    #the line is split into strings using the | as the seperator #!AND THE VALUE IS STORED IN THE VARIABLE ENTRIES RIGHT BLOODY HERE!
    entries = line.split('|')
    print(entries)
   #ENTRIES contains each line as a list with the contents as strings. salesperson is the variable that is assigned to the first string in each list
    salesperson = entries[0]
    #melons is the variable assigned to the third string in each list, and is wrapped in int() to convert the string to a number
    melons = int(entries[2])
    #lthis is a hashmap. 
    if salesperson in salespeople:
        #this I do not understand. is position an operator or a randomly picked variable name? and this looks like it's a key value pair but it's a list, not a dictionary. 
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
       #this adds salesperson and melons to the hashmap if they aren't already there 
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

#the for loop which iterate over the list a number of times that is equal to the length of the list
 for i in range(len(salespeople)):
    #prints the hashmap out in a readable format
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') 