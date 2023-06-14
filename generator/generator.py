import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 80000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address()
    )


def generated_file():
    path = rf'/Users/azubov/Downloads/file_test_{random.randint(1, 100)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World!{random.randint(1, 100)}')
    file.close()
    return file.name, path
