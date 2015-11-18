##
# Kathryn Rodgers
#  16 Nov 2015
##

from  bs4 import BeautifulSoup
import urllib
from lxml.html import parse
import sys
import re

baseAddress = "https://en.wikipedia.org"

def getTitle(soup):
    """
    Gets the title out of a Wikipedia page, given the 
    BeautifulSoup object
    """
    title = soup.title.text
    start = title.find("-")
    return title[:start].strip()


def is_followable_link(tag):
    """
    Takes a tag object from Beautiful Soup and returns if 
    the tag is a link within a paragraph, but not in a table
    and is a link that we'd want to follow
    """
    parents = [p.name for p in tag.parents]
    attr = tag.attrs.get('href', 'cite')
    goodLink = not (":" in attr or "cite" in attr or "#" in attr) and (None != re.match("^/wiki/", attr))
    # if goodLink:
    #     print attr
    return tag.name == "a" and "p" in parents and not("table" in parents) and goodLink


def getFirstLink(soup, visited):
    """
    Gets the first link out of the first paragraph in a  Wikipedia 
    page, given the html text a BeautifulSoup object, and a set of already seen
    pages.
    """
    possibleLinks = soup.find_all(is_followable_link)

    alreadySeen = True
    linkNotGood = True
    for l in possibleLinks:
        link = l.attrs['href']
        if not(link in visited):
            visited.add(link)
            break
    return baseAddress+ link


def start(startURL = "https://en.wikipedia.org/wiki/CodeHS"):
    """
    Starts following links from the given wikipedia page URL
    """ 
    title = ""
    hops = set()
    numHops = 0
    print "Hops made: "
    while title != "Philosophy":
        siteSocket= urllib.urlopen(startURL)
        pageSrc = siteSocket.read()
        siteSocket.close()
        soup = BeautifulSoup(pageSrc, "lxml")
        title =  getTitle(soup)
        print title
        startURL = getFirstLink(soup, hops)
        numHops += 1 
    return numHops

if __name__ == "__main__":

    if len(sys.argv) == 2 :
        startURL = sys.argv[1]
    else:
        startURL = raw_input("What wikipedia page do you want to start with? ")

    invalid = True
    if baseAddress in startURL:
        try:
            urllib.urlopen(startURL)
            invalid = False
        except:
            invalid = True
    # Get a valid starting URL
    while invalid:
        print "Invalid start address. Try that again."
        startURL = raw_input("What wikipedia page do you want to start with? ")
        invalid = not(baseAddress in startURL)
        try:
            urllib.urlopen(startURL)
        except:
            invalid = True
    
    numHops = start(startURL)
    print "It took " + str(numHops) + " page hops to get to Philosophy"

            
