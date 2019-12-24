from nose.tools import *
import wiki_reader.wiki_reader

def setup():
    print 'SETUP!'

def test_remove_refs():
    test_string_before = 'Shrek <ref>3f1w sdf 1we 1wd sd fredref</ref>and Donkey'
    test_string_after = 'Shrek and Donkey'
    result = wiki_reader.wiki_reader.remove_refs(test_string_before)
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
        assert_equal(wiki_reader.wiki_reader.remove_end_sections(before), after)

def teardown():
    print 'TEAR DOWN!'

def test_basic():
    print 'I RAN!'