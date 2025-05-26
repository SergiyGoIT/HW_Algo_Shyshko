from collections import deque

def is_palindrome(input_string):
    # Попередня обробка рядка: прибрати пробіли, перетворити на нижній регістр
    cleaned = ''.join(char.lower() for char in input_string if char.isalnum())

    # Створити двосторонню чергу з очищеного рядка
    char_deque = deque(cleaned)

    # Порівнювати символи з обох кінців deque
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False  # Якщо символи не збігаються — це не паліндром

    return True  # Усі символи збіглися — це паліндром

print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Not a palindrome"))             # False
