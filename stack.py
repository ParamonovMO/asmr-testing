class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавляет элемент на вершину стека."""
        self.items.append(item)

    def pop(self):
        """Удаляет и возвращает элемент с вершины стека.
        Вызывает исключение, если стек пуст."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Возвращает элемент на вершине стека без его удаления.
        Вызывает исключение, если стек пуст."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Проверяет, пуст ли стек."""
        return len(self.items) == 0

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self.items)
