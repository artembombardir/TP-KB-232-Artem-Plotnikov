import pytest
from lab2 import add_new_student, delete_student, update_student

@pytest.fixture(autouse=True)
def setup_students():
    """Автоматично виконується перед кожним тестом та ініціалізує список студентів."""
    global students
    students = [
        {"name": "Alice", "phone": "12345", "email": "alice@example.com", "group": "KB-231"},
        {"name": "Bob", "phone": "67890", "email": "bob@example.com", "group": "KB-245"},
        {"name": "Charlie", "phone": "112233", "email": "charlie@example.com", "group": "KB-213"}
    ]

def test_add_new_student(monkeypatch):
    inputs = iter(["Dave", "99999", "dave@example.com", "KB-299"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    add_new_student()

    assert len(students) == 4
    assert students[-1] == {
        "name": "Dave",
        "phone": "99999",
        "email": "dave@example.com",
        "group": "KB-299"
    }

def test_delete_student(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Alice")

    delete_student()

    assert len(students) == 2
    assert not any(student["name"] == "Alice" for student in students)

def test_update_student(monkeypatch):
    inputs = iter(["Charlie", "Charles", "114455", "charles@example.com", "KB-299"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    update_student()

    assert len(students) == 3
    updated_student = next((s for s in students if s["name"] == "Charles"), None)
    assert updated_student is not None
    assert updated_student["phone"] == "114455"
    assert updated_student["email"] == "charles@example.com"
    assert updated_student["group"] == "KB-299"
