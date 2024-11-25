import pytest


class TestStack:

    def test_init_create_stack(self, create_stack):
        assert create_stack.items == []

    @pytest.mark.parametrize('value', ['a', 'b', 'c', 1, 2, 3, 1000, 9999, True, False])
    def test_push(self, create_stack, value):
        create_stack.push(value)
        assert value in create_stack.items

    @pytest.mark.parametrize('value', ['a', 'b', 'c', 1, 2, 3, 1000, 9999, True, False])
    def test_pop(self, create_stack, value):
        create_stack.push(value)
        a_pop = create_stack.pop()
        assert a_pop == value and create_stack.items == []

    def test_pop_empty(self, create_stack):
        with pytest.raises(IndexError, match='pop from empty stack'):
            create_stack.pop()

    def test_peek(self, create_stack):
        create_stack.push(1)
        create_stack.push(True)
        assert create_stack.peek() == True

    def test_peek_error(self, create_stack):
        with pytest.raises(IndexError, match='peek from empty stack'):
            create_stack.peek()

    def test_is_empty(self, create_stack):
        assert create_stack.is_empty() == 1

    @pytest.mark.parametrize('value, size', [('abc', 1), ('123', 1), (True, 1)])
    def test_size(self, create_stack, value, size):
        create_stack.push(value)
        assert create_stack.size() == size
