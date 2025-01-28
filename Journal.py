import argparse
from datetime import datetime

# Список для хранения действий
records = []

def write_to_file(description, category, time):
    with open("records.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        line = f"[{timestamp}] {time}h {category} {description}\n"
        file.write(line)
# Функция для добавления действия
def add_record(description, category, time):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    records.append({"record": description, "timestamp": timestamp})
    write_to_file(description, category, time)
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
    subparsers = parser.add_subparsers(dest="command", help="Команда для выполнения")
    add_parser = subparsers.add_parser("add", help="Добавить действие")
    add_parser.add_argument("-d", "--description", required=True, help="Текст записи")
    add_parser.add_argument("-c", "--category", choices=["RAMS", "MEET", "WORK", "PLAN", "TARO", "CODING", "READING"], required=True, help="Категория записи")
    add_parser.add_argument("-t", "--time", type=int, required=True, help="Потраченное время в часах")
    show_parser = subparsers.add_parser("show", help="Показать действия")

    args = parser.parse_args()

    if args.command == "add":
        if args.description and args.category and args.time:
            add_record(args.description, args.category, args.time)
        else:
            print(f"Описание '{args.description}' или категория '{args.category}' или время '{args.time}' не были указаны для комманды 'add'")
    elif args.command == "show":
        show_records()
    else:
        print("Для команды 'add' нужно указать действие с помощью параметра '-d' '-c' или '-t'.")

if __name__ == "__main__":
    main()
