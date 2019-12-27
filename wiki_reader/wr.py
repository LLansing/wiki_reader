#!/usr/bin/env python
from sys import argv
from mwclient import *
import re


CURLY_WORDS = [
        'Citation',
        'see also',
        'Relevance',
        'cn'
    ]


def clean_text(text):
    """Clean the text and return it in a more readable format"""
    text = remove_preamble(text)
    text = remove_end_sections(text)
    text = remove_images(text)
    text = remove_refs(text)
    text = remove_links(text)
    text = remove_curlies(text)
    return text

def remove_preamble(text):
    """Remove anything preceding the first text paragraph
       This includes infoboxes that appear near the top of the page"""
    return text[text.find("'''"):]

def remove_end_sections(text):
    """Remove all text following 'See also' or 'References' sections"""
    clipIndex = text.rfind('==See also==')
    clipIndex = clipIndex if clipIndex != -1 else text.rfind('==References==')
    return text[:clipIndex] if clipIndex != -1 else text

def remove_images(text):
    """Remove Images or files and their associated text"""
    drop = re.sub('^\[\[(Image|File).*$','', text, flags=re.MULTILINE)
    return drop

def remove_refs(text):
    """Remove all in-text references"""
    temp = re.sub('\<ref.*?\<\/ref\>', '', text)
    return re.sub('\<ref.*?>', '', temp)

def remove_links(text):
    """Reformat the in-text links"""
    temp = re.sub('\[\[[^\]]*?\|(.*?)\]\]', '\g<1>', text)
    return re.sub('\[\[(.*?)\]\]', '\g<1>', temp)

def remove_curlies(text):
    """Remove the curly braces containing 'Citation needed', etc.
       The first words in the braces to be removed are kept in the CURLY_WORDS list"""
    words = '|'.join(CURLY_WORDS)   
    return re.sub('\{\{(%s).*?\}\}' % words, '', text)
    

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
    f = open('%s.txt' % page_title, 'w+')
    f.write(text.encode('utf8'))
    f.close()


