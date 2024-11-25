import pytest
from stack import Stack


@pytest.fixture
def create_stack():
    stack = Stack()
    return stack
