def read_text():
    quotes = open(r"D:\Udacity\FullStackDeveloper-UdacityNanodegree\Profanity Filter\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

def check_profanity(text_to_check):
    urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
read_text()
