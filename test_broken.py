#!/usr/bin/env python3

# To run the tests, use: python3 -m pytest --capture=sys

from database import Database
from test_database import make_extra_counts

extra_counts = make_extra_counts()
tuple_store = False
try:
    Database.MAX_ID  # Old Database makes db.__MAX_ID private
    tuple_store = True
except AttributeError:
    pass

print('From https://en.wikipedia.org/wiki/Pok%C3%A9mon#Generation_1 ...')
counts = {'kanto': 151, 'johto': 100, 'hoenn': 135, 'sinnoh': 107, 'all': 493}
for region_name, extra_count in extra_counts.items():
    counts[region_name] += extra_count  # add the extras to the wikipedia counts


def test_extra_length():  # fails: 0 record
    # db = Database()
    # if tuple_store:
    #     assert db.get_region('extra')  # Passes
    # else:
    assert Database().get_extra()  # Fails: returns zero pokemon!'


def test_kanto_length():  # passes
    region_name = 'kanto'
    # db = Database()
    # if tuple_store:
    #    assert len(db.get_region(region_name)) == expected_len  # Fails
    # else:
    assert len(Database().get_kanto()) == counts[region_name]  # Passes


def test_johto_length():  # fails:
    region_name = 'johto'
    # db = Database()
    # if tuple_store:
    #    assert len(db.get_region(region_name)) == expected_len  # Fails
    # else:
    assert len(Database().get_johto()) == counts[region_name]  # Passes


def test_hoenn_length():  # fails:
    region_name = 'hoenn'
    # db = Database()
    # if tuple_store:
    #    assert len(db.get_region(region_name)) == expected_len  # Fails
    # else:
    assert len(Database().get_hoenn()) == counts[region_name]  # Passes


def test_sinnoh_length():  # fails:
    region_name = 'sinnoh'
    # db = Database()
    # if tuple_store:
    #    assert len(db.get_region(region_name)) == expected_len  # Fails
    # else:
    assert len(Database().get_sinnoh()) == counts[region_name]  # Passes
