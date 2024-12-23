import pytest
from phonebook_lab2 import add_new, update_entry, delete_entry, load_from_csv, save_to_csv

def test_add_new():
    initial_length = len(phonebook)
    add_new({"name": "Alice", "phone": "0987654321", "email": "alice@gmail.com", "group": "KB-232"})
    assert len(phonebook) == initial_length + 1

def test_update_entry():
    update_entry("Bob", {"phone": "1234567890"})
    assert phonebook[0]["phone"] == "1234567890"

def test_delete_entry():
    delete_entry("Emma")
    assert all(entry["name"] != "Emma" for entry in phonebook)