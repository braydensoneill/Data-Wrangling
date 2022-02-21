#PYTHON 3.8.10

#All work is own, using the previous lab tutorials as guidance, unless stated
#otherwise

#These imports allow for the reading/writing of csv's and twitter scraping
import tweepy as tw
import csv

#Twitter API credentials
consumer_key = "5rNBRZuewDCQUCBmWa6PXym3G"
consumer_secret = "SH4D6kmZcGc2ofTi0GvfHCEi52DRTasiwXbo7OQpY4qYCRFOiR"
access_key = "47300789-PbdTu2I4n91JNh9m1Qm97yWQurLQhlRmaZC5bvTNO"
access_secret = "VI2nFFASrNRj1hwp9MeyIhVFOupgYWpxjumWwQeItUsik"
    
#authorize twitter, initialize tweepy
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tw.API(auth)

#Allow the user to input which word or hashtag they would like to search for.
search_input = input("Enter word or hashtag to search: ")

#The file will be created with a name based on the item searched
filename = search_input

#Allow the user to input have many tweets they would like to search for
search_num_input = input("Enter total tweets to search: ")
search_num = int(search_num_input)

#Print something to show that operations are taking place so that the user does not
#think the window is frozen while searching. 
print("Searching..")


#The next line was created with the use of the following links
#https://stackoverflow.com/questions/22469713/managing-tweepy-api-search
#https://stackoverflow.com/questions/69332653/tweepy-why-did-i-receive-attributeerror-for-search
generated_tweets = tw.Cursor(api.search_tweets,q=search_input).items(search_num)

#Convert the tweepy tweets into a 2D array that will be used to populate the csv
sortedtweets = [[tweet.created_at,
              tweet.text.encode("utf-8"),
              tweet.favorite_count,
              tweet.retweet_count]
             for tweet in generated_tweets]

print(sortedtweets)
#Write to a new csv file. The name of the word or hashtag searched will be the name of the file
with open("%s_tweets.csv" % filename, "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Date","Text","Favorites","Retweets"])
    #search_num won't display the right number if there are less tweets than how many were asked for
    count_tweets = 0
    #Write each tweet into their own row in the csv 
    writer.writerows(sortedtweets)
    #Iterate through each tweet in the list of sorted tweets
    for tweet in sortedtweets:
        #Keep track of how many tweets are being searched for
        count_tweets = count_tweets + 1
    print()        
    print(search_input + "_tweets.csv created. " + str(count_tweets) + " tweets found")

