##### Summary of how I achieved and what I've done to achieve the outcomes of my program

In this specification, I manipulate the data inside book.txt where I return frequency values of the word and for which word. Firstly, from resources, I moved the file into my specification 1 folder so the pathing would allow for my code to run and use the data inside and return values however I also had to edit configurations and put the script paths in (book.txt and my output file (frequencies.csv)).

To start off with, I converted every word in the file to lower case characters by recompiling the file in order to stop repeats of words due to a capital letter. And I also took away punctuation in case some of the same words would have it ("i'm" and "im"). I also found out that I could stop the program from counting spaces by adding a line of code for bad chars and telling the program to recognise space as a bad character so it wouldn't include it in its frequency count

I made a counter function to count the number of times either a word is repeated or a single character which doesn't include any punctuation. 

I then open the input file and perform the analyse frequency function on it where I will then output the word frequencies into a csv file and just print my character frequencies. However I then plot a graph of my character frequencies by zipping the data inside the char_frequency where there are two values so when plotting a graph, it will unpack the iterator into two tuples and puts it as the first two arguments which the program will then recognise and be able to plot them 
