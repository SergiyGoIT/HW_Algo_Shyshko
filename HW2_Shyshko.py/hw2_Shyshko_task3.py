def check_delimiters(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '([{':
            stack.append(char)  # Відкриваюча дужка — додаємо в стек
        elif char in ')]}':
            if not stack:
                return "Несиметрично — закриваюча дужка без відповідної відкриваючої"
            top = stack.pop()
            if pairs[char] != top:
                return f"Несиметрично — не співпадають дужки {top} та {char}"

    if stack:
        return "Несиметрично — лишились відкриті дужки"
    return "Симетрично"


# Приклади використання
examples = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for ex in examples:
    result = check_delimiters(ex)
    print(f"{ex}: {result}")
