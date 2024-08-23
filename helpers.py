import random


class Helpers:
    @staticmethod
    def generate_name():
        names = ['Иван', 'Сергей', 'Василий', 'Михаил']
        generated_name = f'{random.choice(names)}'
        return generated_name

    @staticmethod
    def generate_surname():
        surnames = ['Иванов', 'Петров', 'Сидоров', 'Вайнштейн']
        generated_surname = f'{random.choice(surnames)}'
        return generated_surname

    @staticmethod
    def generate_address():
        addresses = ['Проспект Ленина, 1', 'Хогвартс, Дамблдору', 'Деду на деревню', 'Вишневая 15']
        generated_address = f'{random.choice(addresses)}'
        return generated_address

    @staticmethod
    def generate_number_for_metro_station():
        generated_number = f'{random.randint(0, 9)}'
        return generated_number

    @staticmethod
    def generate_phone_number():
        generated_phone_number = f'{random.randint(10000000000, 999999999999)}'
        return generated_phone_number
