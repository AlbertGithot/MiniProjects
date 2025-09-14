# # enumerate — даёт индекс + элемент
# fruits = ["яблоко", "банан", "груша"]
# for i, fruit in enumerate(fruits, start=1):
#     print(i, fruit)
# # 1 яблоко
# # 2 банан
# # 3 груша
# # 🛠 Пригодится: когда надо нумеровать элементы списка (например, вывод меню или таблицы).
#

# /===/
#
# # filter — фильтрует список по условию
# nums = [1, 2, 3, 4, 5]
# even = list(filter(lambda x: x % 2 == 0, nums))
# print(even)  # -> [2, 4]
# # 🛠 Пригодится: отобрать только нужные элементы (например, только активные пользователи из базы).
#
# /===/
#
# # map — применяет функцию ко всем элементам
# nums = [1, 2, 3]
# squared = list(map(lambda x: x**2, nums))
# print(squared)  # -> [1, 4, 9]
# # 🛠 Пригодится: преобразовать все элементы (например, перевести текст в верхний регистр).
#

# /===/



# a = []
# for i in range(99):
#     if i % 2 == 0:
#         a.append(i)
# print(a)
# b = [i  if i % 2 == 0 else print('это нечетное') for i in range(99)]
# print(b)

# spisok = [i for i in range(0, 101, 5)]
# print(spisok)

# # Родительский класс
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return "Я издаю звук"
#
#
# # Дочерний класс (наследует от Animal)
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} говорит: Гав-гав!"
#
#
# # Ещё один дочерний класс
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} говорит: Мяу!"
#
#
# # Используем
# dog = Dog("Бобик")
# cat = Cat("Мурка")
#
# print(dog.speak())  # Бобик говорит: Гав-гав!
# print(cat.speak())  # Мурка говорит: Мяу!

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner        # публичное
#         self._balance = balance   # защищённое
#         self.__pin = "1234"       # приватное
#
#     def deposit(self, amount):
#         self._balance += amount
#         return f"Баланс пополнен, теперь: {self._balance}"
#
#     def withdraw(self, amount, pin):
#         if pin == self.__pin:
#             if amount <= self._balance:
#                 self._balance -= amount
#                 return f"Вы сняли {amount}. Остаток: {self._balance}"
#             else:
#                 return "Недостаточно средств"
#         else:
#             return "Неверный PIN"
#
# acc = BankAccount("Паша", 1000)
# acc.owner = "Marselos"
# print(acc.owner)
# acc._balance = 100
# print(acc._balance)
# acc.__pin = "4444"
# print(acc.__pin)
#
#
#
#
#
#
#
#
#
# print(acc.deposit(500))              # Баланс пополнен, теперь: 1500
# print(acc.withdraw(300, "1234"))     # Вы сняли 300. Остаток: 1200
#
# print(acc.owner)      # Публичное → можно напрямую
# print(acc._balance)   # Можно, но лучше не трогать напрямую
# # print(acc.__pin)    # Ошибка! приватное
#
# # Но на самом деле оно спрятано как _BankAccount__pin
# print(acc._BankAccount__pin)  # 1234 (но так лучше не делать!)
#


# class Hero:
#     def attack(self):
#         return "Герой атакует!"
#
#
# class Knight(Hero):
#     def attack(self):
#         return "Рыцарь машет мечом ⚔️"
#
#
# class Archer(Hero):
#     def attack(self):
#         return "Лучник стреляет из лука 🏹"
#
#
# class Wizard(Hero):
#     def attack(self):
#         return "Маг запускает огненный шар 🔥"
#

# class Plant:
#     self.hp = ...
#
#     def update(self):
#     def kill(self):
#
# class SunFlower(Plant):
#     pass
#
# class PeaShooter(Plant):
#     pass
#
# plant1 = PLant()