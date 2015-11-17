##
# Kathryn Rodgers
#  16 Nov 2015
##

import urllib
from lxml.html import parse

baseAddress = "https://en.wikipedia.org"

def getTitle(htmlPage):
    """
    Gets the title out of a Wikipedia page, given the html text in htmlPage
    """
    start = htmlPage.find("<title>") + len("<title>")
    end = htmlPage.find("- Wikipedia")
    return htmlPage[start:end]


def getFirstLink(htmlPage):
    """
    Gets the first link out of the first paragraph in a  Wikipedia 
    page, given the html text in htmlPage
    """
    start = htmlPage.find("<p")  # find first paragraph
    
    link = "Help:"
    while "Help:" in link: # ignore the prounounciation links
        linkStart = htmlPage.find("<a href=\"/wiki", start) + len("<a href=\"")
        linkEnd= htmlPage.find("\"", linkStart+1)
        link = htmlPage[linkStart:linkEnd]
        start = linkStart
    return baseAddress+ link


def start(startURL = "https://en.wikipedia.org/wiki/CodeHS"):
    """
    Starts following links from the given wikipedia page URL
    """ 
    title = ""
    print "Hops made: "
    while title != "Philosophy":
        siteSocket= urllib.urlopen(startURL)
        pageSrc = siteSocket.read()
        title =  getTitle(pageSrc).strip()
        print title
        startURL = getFirstLink(pageSrc)

if __name__ == "__main__":
    startURL = raw_input("What wikipedia page do you want to start with? ")
    invalid = not(baseAddress in startURL)
    try:
        urllib.urlopen(startURL)
    except:
        invalid = True
    # Get a valid starting URL
    while invalid:
        print "Invalid start address. Try that again: "
        startURL = raw_input("What wikipedia page do you want to start with? ")
        invalid = not(baseAddress in startURL)
        try:
            urllib.urlopen(startURL)
        except:
            invalid = True
    
    start(startURL)
            
            
