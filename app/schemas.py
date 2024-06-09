from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from models import TodoItem


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: int = 0
    done: bool = False
    due_date: Optional[datetime.date] = None


class TodoCreate(TodoBase):
    due_date: Optional[datetime.date] = Field(default_factory=TodoItem.set_end_of_day)
