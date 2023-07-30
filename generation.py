import random
import string

GENDER = ['m', 'f']


def generate_users():
    letters = string.ascii_lowercase
    length = random.randint(3, 30)
    name = ''.join(random.choice(letters) for _ in range(length))
    length = random.randint(3, 30)
    second_name = ''.join(random.choice(letters) for _ in range(length))
    length = random.randint(3, 30)
    father_name = ''.join(random.choice(letters) for _ in range(length))
    year = random.randint(1899, 2023)
    month = str(random.randint(1, 12))
    day = str(random.randint(1, 27))
    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    yield second_name.title(), name.title(), father_name.title(), f'{year}-{month}-{day}', random.choice(GENDER)


def generate_users_with_f():
    letters = string.ascii_lowercase
    length = random.randint(3, 30)
    name = ''.join(random.choice(letters) for _ in range(length))
    length = random.randint(3, 30)
    second_name = ''.join(random.choice(letters) for _ in range(length))
    length = random.randint(3, 30)
    father_name = ''.join(random.choice(letters) for _ in range(length))
    year = random.randint(1899, 2023)
    month = str(random.randint(1, 12))
    day = str(random.randint(1, 27))
    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    yield 'F' + second_name, name.title(), father_name.title(), f'{year}-{month}-{day}'
