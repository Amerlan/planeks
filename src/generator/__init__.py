from faker import Faker
from random import randrange


fake = Faker()


def sentence(*, qty: int, string_char: str, separator: str):
    text = f'{string_char}'
    for x in range(qty):
        text += fake.sentence() + ' '
    text += f'{string_char}'.replace(f'{separator}', '')
    return text


def integer(*, lower: int, upper: int):
    return randrange(lower, upper)


def address():
    return fake.address().replace('\n', ' ')

column_types = {
    1: fake.name,
    2: fake.job,
    3: fake.email,
    4: fake.url,
    5: fake.phone_number,
    6: fake.company,
    7: sentence,
    8: integer,
    9: address,
    10: fake.date,
}
