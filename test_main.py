#!/usr/bin/env python3

# To run the tests, use: python3 -m pytest --capture=sys

from collections import namedtuple
from database import Database
from main import main
import pytest

region_record = namedtuple('region_record', 'roman_number start end')
region_dict = {
    "kanto": region_record("I", 1, 151),
    "johto": region_record("II", 152, 251),
    "hoenn": region_record("III", 252, 386),
    "sinnoh": region_record("IV", 387, 493),
    "extra": region_record("", 494, 100000)
}

tuple_store = False
db = Database()
print(len(db))
try:
    print(len(db.get_kanto()))
    print(len(db.get_johto()))
    print(len(db.get_hoenn()))
    print(len(db.get_sinnoh()))
    print(len(db.get_extra()))
except AttributeError:
    tuple_store = True


def test_no_args(capsys):
    try:
        with pytest.raises(SystemExit):
            main([__file__])
    except SystemExit:
        pass
    out, err = capsys.readouterr()
    assert out.startswith("No command line arguments specified.")


def test_three_args(capsys):
    main([__file__, 1, 2, 3])
    out, err = capsys.readouterr()
    assert out.startswith("Invalid number of arguments.")
