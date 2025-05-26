import queue

# Створити чергу заявок
request_queue = queue.Queue()
request_id = 1  # Унікальний номер заявки

# Функція generate_request()
def generate_request():
    global request_id
    new_request = f"Заявка №{request_id}"
    request_queue.put(new_request)
    print(f"Згенеровано: {new_request}")
    request_id += 1

# Функція process_request()
def process_request():
    if not request_queue.empty():
        current_request = request_queue.get()
        print(f"Оброблено: {current_request}")
    else:
        print("Черга порожня. Немає заявок для обробки.")

# Головний цикл програми
def main():
    print("СИСТЕМА ОБРОБКИ ЗАЯВОК (ВВЕДІТЬ 1 - згенерувати, 2 - обробити, 0 - вийти)")
    while True:
        command = input("Введіть команду (1/2/0): ")
        if command == "1":
            generate_request()
        elif command == "2":
            process_request()
        elif command == "0":
            print("Завершення роботи програми.")
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
