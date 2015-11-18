# Get to Philosophy
*Finding philosophy*

### Project Description
This project is inspired by the tooltip text of this xkcd comic: http://xkcd.com/903/

Write a program that takes in a Wikipedia page and follows the first
link on the page until it reaches the Wikipedia page for the
Philosophy article. The program should list out each hop it takes and
print out the total number of hops at the end.

![Getting to Philosophy](/CodeHS_to_Philosophy.png)


# My Solution 
My solution source is in the folder src.  It's a python
file. You can run it by passing the start page as a command line parameter: 

python crawler.py https://en.wikipedia.org/the-page-to-start-on

or run it and it will prompt you to enter the starting page

# Requirements
This was tested with Python version 2.7.  It also requires Beautiful
Soup version 4 (http://www.crummy.com/software/BeautifulSoup/)