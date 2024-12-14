# Тема 1. Домашня робота

Прийшов час практики. У домашній роботі буде два завдання.

В обох завданнях необхідно застосувати типізацію. Замість оператора `print` слід використовувати логування на рівні `INFO`. Для форматування коду використовуйте **black**.

**Технічний опис завдань**

## Завдання 1. Патерн фабрика

Наступний код представляє просту систему для створення транспортних засобів. У нас є два класи: `Car` та `Motorcycle`. Кожен клас має метод `start_engine()`, який імітує запуск двигуна відповідного транспортного засобу. Наразі, щоб створити новий транспортний засіб, ми просто створюємо екземпляр відповідного класу з вказаними маркою (`make`) та моделлю (`model`).

```Py
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")

class Motorcycle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")

# Використання
vehicle1 = Car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = Motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
```

<button class="copy"></button>

Наступним кроком потрібно створювати транспортні засоби з урахуванням специфікацій різних регіонів наприклад, для США `US Spec` та ЄС `EU Spec`.

**Ваше завдання** — реалізувати патерн фабрика, який дозволить створювати транспортні засоби з різними регіональними специфікаціями, не змінюючи основні класи транспортних засобів.

**Ход виконання завдання 1:**

1. Створити абстрактний базовий клас `Vehicle` з методом `start_engine()`.
2. Змінити класи `Car` та `Motorcycle`, щоб вони успадковувались від `Vehicle`.
3. Створити абстрактний клас `VehicleFactory` з методами `create_car()` та `create_motorcycle()`.
4. Реалізувати два класи фабрики: `USVehicleFactory` та `EUVehicleFactory`. Ці фабрики повинні створювати автомобілі та мотоцикли з позначкою регіону наприклад, `Ford Mustang (US Spec)` відповідно для США.
5. Змініть початковий код так, щоб він використовував фабрики для створення транспортних засобів.

**Очікуваний результат**

- Код, що дозволяє легко створювати транспортні засоби для різних регіонів, використовуючи відповідні фабрики.

## Рішення 1

[task_1.py](goit_pythonweb_hw_01/task_1.py)

Результати роботи:

```log
/goit-pythonweb-hw-01/goit_pythonweb_hw_01/task_1.py
2024-12-14 04:40:50,175 - INFO - # --------- Використання без фабрики: ---------
2024-12-14 04:40:50,175 - INFO - Toyota Corolla: Двигун запущено
2024-12-14 04:40:50,175 - INFO - Harley-Davidson Sportster: Мотор заведено
2024-12-14 04:40:50,176 - INFO - # --------- Використання з фабриками: ---------
2024-12-14 04:40:50,176 - INFO - Ford Mustang (US Spec): Двигун запущено
2024-12-14 04:40:50,176 - INFO - Harley-Davidson Sportster (US Spec): Мотор заведено
2024-12-14 04:40:50,176 - INFO - Volvo V40 (EU Spec): Двигун запущено
2024-12-14 04:40:50,176 - INFO - BMW R1200GS (EU Spec): Мотор заведено
2024-12-14 04:40:50,176 - INFO - Volvo V90 (US Spec): Двигун запущено
2024-12-14 04:40:50,177 - INFO - BMW S1000R (US Spec): Мотор заведено
```

## Завдання 2. SOLID

Перед вами спрощена програма для керування бібліотекою книг. Програма має можливість додавання нових книг, видалення книг та відображення всіх книг у бібліотеці. Користувач має змогу взаємодіяти з програмою через командний рядок, використовуючи команди `add`, `remove`, `show` та `exit`.

```Py
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        book = {
            "title": title,
            "author": author,
            "year": year
        }
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                break

    def show_books(self):
        for book in self.books:
            print(f'Title: {book["title"]}, Author: {book["author"]}, Year: {book["year"]}')

def main():
    library = Library()

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter book year: ").strip()
            library.add_book(title, author, year)
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            library.remove_book(title)
        elif command == "show":
            library.show_books()
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
```

**Ваше завдання** — переписати код, щоб він відповідав принципам SOLID.

## Рішення 2

[task_2.py](goit_pythonweb_hw_01/task_2.py)
