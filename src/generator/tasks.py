from celery import shared_task
from .models import Schema, Column
from . import column_types


@shared_task
def generate_csv(qty: int, schema: Schema):
    with open(f'media/{schema.name}.csv', 'w') as file:
        columns = Column.objects.filter(schema=schema.id)
        separator = schema.separator
        string_char = schema.string_character
        header = ''
        for column in columns:
            header += f'{column.name}{separator}'
        file.write(header+'\n')
        for j in range(qty):
            row = ''
            for column in columns:
                field_type = column.field_type
                upper = column.upper_bound
                lower = column.lower_bound
                sentence_count = column.sentence_count
                generator = column_types[field_type]
                if field_type == 7:
                    row += f'{generator(qty=sentence_count, string_char=string_char)}'
                elif field_type == 8:
                    row += f'{generator(lower=lower, upper=upper)}'
                else:
                    row += generator()
                row += separator
                print(row)
            file.write(row+'\n')



