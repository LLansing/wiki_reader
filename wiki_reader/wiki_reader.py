#!/usr/bin/env python
from sys import argv
from mwclient import *
import re


def clean_text(text):
    text = remove_refs(text)
    text = remove_end_sections(text)
    return text


def remove_end_sections(text):
    # Removes all sections after See also or References
    clipIndex = text.rfind('==See also==')
    clipIndex = clipIndex if clipIndex != -1 else text.rfind('==References==')
    return text[:clipIndex] if clipIndex != -1 else text

def remove_refs(text):
    return re.sub('\<ref\>.*?\<\/ref\>', '', text)


if __name__ == "__main__":
    script, page_title = argv

    # get the site object for wikipedia
    site = Site('en.Wikipedia.org')

    # get page with given title from the site
    page = site.pages[page_title]
    # get the text from the page
    text = page.text()
    # filter text
    text = clean_text(text)

    # write output to file
    f = open('temp_output.txt', 'w+')
    f.write(text.encode('utf8'))
    f.close()

    print text

