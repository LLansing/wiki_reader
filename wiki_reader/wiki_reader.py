#!/usr/bin/env python
from sys import argv
from mwclient import *
import re


def clean_text(text):
    """Clean the text and return it in a more readable format"""
    text = remove_end_sections(text)
    text = remove_images(text)
    text = remove_refs(text)
    return text


def remove_end_sections(text):
    """Remove all text following 'See also' or 'References' sections"""
    clipIndex = text.rfind('==See also==')
    clipIndex = clipIndex if clipIndex != -1 else text.rfind('==References==')
    return text[:clipIndex] if clipIndex != -1 else text

def remove_images(text):
    """Remove Images and their associated text"""
    drop = re.sub('^\[\[Image.*$','', text, flags=re.MULTILINE)
    print drop
    return drop

def remove_refs(text):
    """Remove all in-text references"""
    temp = re.sub('\<ref.*?\<\/ref\>', '', text)
    return re.sub('\<ref.*?>', '', temp)


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


