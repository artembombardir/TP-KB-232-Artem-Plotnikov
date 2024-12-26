import pytest
from lab2 import add_student, delete_student, update_student, read_from_csv, write_to_csv, students

@pytest.fixture(autouse=True)
def setup_students():
    """Fixture to reset the global students list before each test."""
    students.clear()

def test_add_student():
    add_student("Alice", "12345", "alice@example.com", "Group1")
    assert len(students) == 1
    assert students[0]["name"] == "Alice"

def test_delete_student():
    add_student("Alice", "12345", "alice@example.com", "Group1")
    delete_student("Alice")
    assert len(students) == 0

def test_update_student():
    add_student("Alice", "12345", "alice@example.com", "Group1")
    update_student("Alice", new_phone="67890")
    assert students[0]["phone"] == "67890"

def test_read_write_csv():
    add_student("Alice", "12345", "alice@example.com", "Group1")
    write_to_csv("test_output.csv")
    students.clear()  # Clear the list to simulate reading from file
    read_from_csv("test_output.csv")
    assert len(students) == 1
    assert students[0]["name"] == "Alice"
