import argparse
from datetime import datetime

# Список для хранения действий
records = []

# Функция для добавления действия
def add_record(description, category, time):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    records.append({"record": description, "timestamp": timestamp})
    print(f"'{description}' добавлено в {timestamp} with category {category} and time {time}")

# Функция для отображения действий
def show_records():
    if records:
        print("Записанные действия:")
        for entry in records:
            print(f"- {entry['record']} (время: {entry['timestamp']})")
    else:
        print("Нет записанных действий.")

# Основная функция
def main():
    parser = argparse.ArgumentParser(description="Отслеживание действий")
    parser.add_argument("command", choices=["add", "show"], help="Команда для выполнения")
    parser.add_argument("-d", "--description", help="Текст записи")
    parser.add_argument("-c", "--category", help="Категория записи")
    parser.add_argument("-t", "--time", help="Потраченное время в часах")

    args = parser.parse_args()

    if args.command == "add" and args.description:
        add_record(args.description, args.category, args.time)
    elif args.command == "show":
        show_records()
    else:
        print("Для команды 'add' нужно указать действие с помощью параметра '-d' '-c' или '-t'.")

if __name__ == "__main__":
    main()
