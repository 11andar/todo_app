import pytest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from app.models import TodoItem
from app.schemas import TodoBase
from app.crud import (
    create_todo,
    get_todo_item,
    get_todos,
    update_todo,
    delete_todo
)


@pytest.fixture
def mock_db():
    return MagicMock(spec=Session)


def test_create_todo(mock_db):
    todo_data = TodoBase(title="Test Todo")
    mock_db.add = MagicMock()
    mock_db.commit = MagicMock()
    mock_db.refresh = MagicMock()

    created_todo = create_todo(mock_db, todo_data)

    assert isinstance(created_todo, TodoItem)
    assert created_todo.title == "Test Todo"
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once_with(created_todo)


def test_get_todo_item(mock_db):
    todo_item = TodoItem(title="Test Todo", id=1)
    mock_db.query.return_value.filter.return_value.first.return_value = todo_item
    result = get_todo_item(mock_db, 1)
    assert result == todo_item