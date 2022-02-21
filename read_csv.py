#!/usr/bin/env python

#PYTHON 3.8.10

#All work is own, using the previous lab tutorials as guidance, unless stated
#otherwise

#These imports allow you to read/write csv's and sort the data accordingly
import csv
import pandas

#Tables were not being fully printed (fields were being displayed as "...")
#I set these options so that you can see all the fields being printed.
#Only show some of the text field before displaying "..." to avoid clutter
pandas.set_option('display.max_rows', 500)
pandas.set_option('display.max_columns', 500)
pandas.set_option('display.width', 1000)

#User decides which file to open. Make sure to type the filename AND type
filename = input("Enter filename to open: ")

#Set the null values for each column I haven't come across any null values
#while testing it, so I set empty strings as null values just incase any are
#found
nullValues = {'Date': [''],
              'Text': [''],
              'Favorites': [''],
              'Retweets': ['']}

#Create a data_field. Read the csv that was entered by the user. Each row in
#the csv will have their own list of data containing the information in the
#each columns. Skip the first row because the first row in the csv contains
#the headings. Consider for null values (if any).
df = pandas.read_csv(filename,
                     names=['Date',
                            'Text',
                            'Favorites',
                            'Retweets'],
                     skiprows=[0],
                     na_values=nullValues)

#Sort the data collected by Date (Ascending/Descending)
date_ascending = df.sort_values(by='Date',ascending=True)
date_descending = df.sort_values(by='Date',ascending=False)

#Sort the data collected by the number of favourites (Ascending/Descending)
favorites_ascending = df.sort_values(by='Favorites',ascending=True)
favorites_descending = df.sort_values(by='Favorites',ascending=False)

#Sort the data collected by the number of retweets (Ascending/Descending)
retweets_ascending = df.sort_values(by='Retweets',ascending=True)
retweets_descending = df.sort_values(by='Retweets',ascending=False)

#Create a loop, allowing for user input, to decide what is printed on screen
choice = 0
while choice != 7:
    print()
    print("Select an option to sort the data:")
    print("    1 - Date (ascending)")
    print("    2 - Date (descending)")
    print("    3 - Favorites (ascending)")
    print("    4 - Favorites (descending)")
    print("    5 - Retweets (ascending)")
    print("    6 - Retweets (descending)")
    print("    7 - Exit")
    
    choice = int(input(""))
    
    if choice == 1: print(date_ascending)
    elif choice == 2: print(date_descending)
    elif choice == 3: print(favorites_ascending)
    elif choice == 4: print(favorites_descending)
    elif choice == 5: print(retweets_ascending)
    elif choice == 6: print(retweets_descending)
    elif choice == 7: print("Goodbye!")
    else: print("Invalid Entry")

