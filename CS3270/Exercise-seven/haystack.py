"""
    Cody Strange
    12/02/2022
    CS3270-001
    Programming project D

    Summary:
            I need to create a program that can crawl through webpages, recording information on the webpage
            and then following the links attached to the webpage to future webpages. While making sure to not crawl
            the same webpage twice.
            This project can be split into six different sections.

            - Section One:
                    Create a program that can crawl through webpages (COMPLETE)
            - Section Two:
                    Create a list of all of the webpages that have been crawled through (COMPLETE)
                        - can use the graph keys for this
            - Section Three:
                    Create a lookup method that takes a word as a search key and 
                    outputs the webpages that contain that word in rank order, highest to lowest.
            - Section Four:
                    Create an index dictionary of all the words found on in all of the crawled webpages.
                    This index will contain more dictionaries where each word is a key and a list
                    the webpages that have each word are the values. (COMPLETE)

                    convert all words to lowercase and only count the words that have alphabetic characters and apostrophes
            - Section Five
                    Create a graph dictionary of all the webpages where the webpage is the key and a list
                    of all webpage links that the webpage has is the key.
            - Section Six
                    Use the provided 'compute_ranks' function


    Bugs:
        - one remaing, ranks slightly off. Don't know why.

    Required features:
        - all

    Recomended features
        - The ranks are slightly off, they are on point enough that the
        lookup method still works fine, and I can't figure out why they are off at all.

"""
from main_test import hay_stack_TEST, crawl_TEST, index_TEST, graph_TEST
import requests
import re
import pprint
class HayStack():
    def __init__(self, url, count):
        self.count = count
        self.url = url
        self.page_list = []
        self.index = {}
        self.graph = {}
        self.crawl(self.url, count)
        self.compute_ranks(self.graph)
    def crawl(self, url, count):
        if count == 0:
            return
        content = requests.get(url, headers={"User-Agent": "XY"}).text
        page_name = re.search('<h1>.+<\/h1>', str(content))
        if page_name.group() in self.page_list:
            pass
        else:
            # """Enter a new webpage"""
            list_links = re.findall('<a href=[^>]+>|<a href = [^>]+>', content)
            self.graph[url] = []
            # Create a graph from the words in the webpages as they are being crawled
            web_tags = re.findall("<\S+>|<a [^>]+>", content) # Removing all the tags from the web_page
            for tag in web_tags:
                content = content.replace(tag, '')
            page_words = re.findall("[a-zA-Z|']+", content) # Create a list of all the words from the web_page
            page_words = {i.lower() for i in page_words}
            page_words = list(page_words)
            page_words.sort()
            for word in page_words: # Map the webpage url to every word that is in its webpage
                if word not in self.index:
                    self.index[word] = [url]
                else:
                    self.index[word].append(url)
            # Add a new webpage to the list of crawled webpages
            self.page_list.append(page_name.group())
            for link in list_links:
                new_url = link.split('"')[1]
                self.graph[url].append(new_url)
                self.crawl(new_url, count - 1)
    def compute_ranks(self, graph):
        d = 0.85 # probability that surfer will bail
        numloops = 10
        ranks = {}
        npages = len(graph)
        for page in graph:
            ranks[page] = 1.0 / npages
        for _ in range(0, numloops):
            newranks = {}
            for page in graph:
                newrank = (1 - d) / npages
                for url in graph: 
                    if page in graph[url]: # this url links to page
                        newrank += d*ranks[url]/len(graph[url])
                newranks[page] = newrank
            ranks = newranks
        self.ranks = ranks
    def lookup(self, word):
        word = word.lower()
        def compare(value):
            self.compute_ranks(self.graph)
            return self.ranks[value]
        word = self.index[word]
        word.sort(reverse=True, key=compare)
        return word
if __name__ == "__main__":
    engine = HayStack('http://roversgame.net/cs3270/page1.html',4)
    for w in ['pages','links','you','have','I']:
        print(w)
        pprint.pprint(engine.lookup(w))
    print()
    print('index:')
    pprint.pprint(engine.index)
    print()
    print('graph:')
    pprint.pprint(engine.graph)
    print()
    print('ranks:')
    pprint.pprint({page:round(rank,4) for page,rank in engine.ranks.items()})