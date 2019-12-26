from nose.tools import *
import wiki_reader


def test_remove_refs():
    test_string_before = 'Shrek <ref>3f1w sdf 1we 1wd sd fredref</ref>and Donkey'
    test_string_after = 'Shrek and Donkey'
    result = wr.remove_refs(test_string_before)
    assert_equal(result, test_string_after)

def test_remove_end_sections():
    test_strings_before = [
        'Everybody loves parfait!\n==See also== This part should be removed',
        'Onions have layers.\n==References== This part should be removed'
    ]

    test_strings_after = [
        'Everybody loves parfait!\n',
        'Onions have layers.\n'
    ]

    for (before, after) in zip(test_strings_before, test_strings_after):
        assert_equal(wr.remove_end_sections(before), after)

def test_remove_images():
    test_string_before = 'Get out of my swamp!\n[[Image: Shrek yelling]]And this should be removed.\nBut...[[Image]] shouldn\'t'
    test_string_after = 'Get out of my swamp!\n\nBut...[[Image]] shouldn\'t'
    assert_equal(wr.remove_images(test_string_before), test_string_after)

def test_remove_links():
    test_strings_before = [
        'That is a nice [[rock|boulder]]!',
        'In the morning, I\'m making [[waffles]]!'
    ]

    test_strings_after = [
        'That is a nice boulder!',
        'In the morning, I\'m making waffles!'
    ]
    
    for (before, after) in zip(test_strings_before, test_strings_after):
        assert_equal(wr.remove_links(before), after)

def test_remove_curlies():
    test_strings_before = [
        'She called me a noble steed.\{\{Citation needed|date=April 2007\}\}',
        'She called me a noble\{\{cn|date=July 2019\}\} steed.',
        '\{\{Relevance inline|date=July 2019\}\}She called me a noble steed.',
        'She called me a noble steed\{\{see also|mount\}\}.'
    ]
    
    s = 'She called me a noble steed.'
    test_strings_after = [s, s, s, s]

    for (before, after) in zip(test_strings_before, test_strings_after):
        assert_equal(wr.remove_curlies(before), after)