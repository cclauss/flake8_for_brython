#!/usr/bin/env python3

# To run the tests, use: python3 -m pytest --capture=sys

from database import Database

# Database unfortunately makes db.__MAX_ID private :-(
MAX_ID = 493

db = Database()
print('From https://en.wikipedia.org/wiki/Pok%C3%A9mon#Generation_1 ...')
counts = {'kanto': 151, 'johto': 100, 'hoenn': 135, 'sinnoh': 107, 'all': 493}


def test_kanto_length():  # passes
    assert len(db.get_kanto()) == 151  # Passes


def test_johto_length():  # fails:
    assert len(db.get_johto()) == 100  # Fails: assert 101 == 100


def test_hoenn_length():  # fails:
    assert len(db.get_hoenn()) == 135  # Fails: assert 144 == 135


def test_sinnoh_length():  # fails:
    assert len(db.get_sinnoh()) == 107  # Fails: assert 121 == 107


def test_extra_length():  # fails: 0 record
    assert db.get_extra()  # Fails: returns zero pokemon!'
