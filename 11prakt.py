import random
import string


def task_1():
    """
    Задача 1: Нахождение общих элементов двух последовательностей и их количества.
    Реализовано с использованием списковых включений и генераторов.
    """
    print("--- Задача 1 ---")
    
    # Задаем размер последовательностей
    n = 15
    
    # Генерируем две исходные последовательности случайных чисел
    seq_a = [random.randint(1, 25) for _ in range(n)]
    seq_b = [random.randint(1, 25) for _ in range(n)]
    
    print(f"Исходная последовательность А: {seq_a}")
    print(f"Исходная последовательность В: {seq_b}")
    
    # Находим общие элементы без дубликатов (используя списковое включение и set для уникальности)
    common_elements = list({x for x in seq_a if x in seq_b})
    
    # Находим количество общих элементов
    count_common = len(common_elements)
    
    print(f"Общие элементы: {common_elements}")
    print(f"Количество уникальных общих элементов: {count_common}")


def task_2():
    """
    Задача 2: Отображение только символов нижнего регистра из заданной строки.
    Используется библиотека string и списковое включение (генератор списка).
    """
    print("\n--- Задача 2 ---")
    
    # Исходная строка по условию варианта
    source_str = "In PyCharm, you can specify third-party standalone applications and run them as External Tools"
    print(f"Исходная строка: '{source_str}'")
    
    # Фильтруем строку: оставляем только символы, которые входят в string.ascii_lowercase
    lowercase_chars = [char for char in source_str if char in string.ascii_lowercase]
    
    # Объединяем символы обратно в строку (или выводим списком, как требует задание)
    result_str = "".join(lowercase_chars)
    
    print(f"Символы нижнего регистра (в виде строки): '{result_str}'")
    print(f"Полученный список символов: {lowercase_chars}")


if __name__ == "__main__":
    task_1()
    task_2()
