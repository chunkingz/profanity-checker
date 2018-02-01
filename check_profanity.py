import urllib

def read_text():
    quotes = open("C:\Users\chun_kingz\Documents\movie_quotes.txt")
    contentsOfFile = quotes.read()
    #print contentsOfFile
    quotes.close()
    check_profanity(contentsOfFile)

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = connection.read()
    #print output
    connection.close()

    if "true" in output:
        print "Profanity Detected!"
    elif "false"in output:
        print "No profane words detected."
    else:
        print "Error reading document."
    
read_text()
