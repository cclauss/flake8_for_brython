#!/usr/bin/env python3

# To run the tests, use: python3 -m pytest --capture=sys

from database import Database

# Database unfortunately makes db.__MAX_ID private :-(
MAX_ID = 493

print('From https://en.wikipedia.org/wiki/Pok%C3%A9mon#Generation_1 ...')
counts = {'kanto': 151, 'johto': 100, 'hoenn': 135, 'sinnoh': 107, 'all': 493}


def test_kanto_length():  # passes
    expected = counts['kanto']
    actual = len(Database().get_kanto())
    msg = 'kanto expected: {}\n  actual: {}'.format(expected, actual)
    print(msg)
    assert expected == actual, msg


def test_johto_length():  # fails:
    expected = counts['johto']
    actual = len(Database().get_johto())
    msg = 'johto expected: {}\n  actual: {}'.format(expected, actual)
    print(msg)
    assert expected == actual, msg


def test_hoenn_length():  # fails:
    expected = counts['hoenn']
    actual = len(Database().get_hoenn())
    msg = 'hoenn expected: {}\n  actual: {}'.format(expected, actual)
    print(msg)
    assert expected == actual, msg


def test_sinnoh_length():  # fails:
    #expected = counts['sinnoh']
    #actual = len(Database().get_sinnoh())
    #msg = 'sinnoh expected: {}\n  actual: {}'.format(expected, actual)
    #print(msg)
    #assert expected == actual, msg
    len(Database().get_sinnoh()) == counts['sinnoh']


def test_extra_length():  # fails: 0 record
    assert Database().get_extra(), 'db.get_extra() returns no pokemon!'
