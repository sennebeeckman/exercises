import pytest
from book import Book


@pytest.mark.parametrize("title, isbn", [("lotr", "978-1-60309-502-0"), ("the hobbit", "978-160309-5174"), ("hunger", "978-1-60309 -527-3")])
def test_valid_creation(title, isbn):
    book = Book(title, isbn)
    assert book.title == title
    assert book.isbn == isbn


@pytest.mark.parametrize("isbn", ["978-1-60309-502-0", "978-160309-5174", "978-1-60309 -527-3"])
def test_creation_with_invalid_title(isbn):
    with pytest.raises(RuntimeError):
        book = Book("", isbn)


@pytest.mark.parametrize("isbn", ["978-1-64309-502-0", "978-160309-51747", "98-1-60309 -527-3"])
def test_creation_with_invalid_isbn(isbn):
    with pytest.raises(RuntimeError):
        book = Book("title", isbn)