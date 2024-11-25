- ** Класс на Stack, который реализует стек (структуру данных)


- **`__init__`**: Инициализирует новый стек, создавая пустой список.
- **`push(item)`**: Добавляет элемент `item` на вершину стека.
- **`pop()`**: Удаляет и возвращает элемент с вершины стека. Если стек пуст, вызывает исключение `IndexError`.
- **`peek()`**: Возвращает элемент на вершине стека без его удаления. Если стек пуст, вызывает исключение `IndexError`.
- **`is_empty()`**: Проверяет, пуст ли стек, возвращая `True` или `False`.
- **`size()`**: Возвращает количество элементов в стеке.

### Входные и выходные данные

- Входные данные: Элементы, которые вы хотите добавить в стек (например, целые числа или строки).
- Выходные данные: 
  - Метод `pop()` возвращает последний добавленный элемент и удаляет его из стека.
  - Метод `peek()` возвращает последний добавленный элемент без удаления.
  - Метод `is_empty()` возвращает `True`, если стек пуст, и `False` в противном случае.
  - Метод `size()` возвращает количество элементов в стеке.


### % покрытия тестов класса
-pytest --cov=stack --cov-branch --cov-report=html

### Запуск тестов
-pytest test_stack.py