from django.db import models


class Schema(models.Model):
    name = models.CharField('Schema name', unique=True, max_length=25)
    separator = models.CharField('Field data separator sign', max_length=1)
    string_character = models.CharField('String character', max_length=1)


class Column(models.Model):
    name = models.CharField('Column name', max_length=25)
    schema = models.ForeignKey('generator.Schema', verbose_name='Schema', on_delete=models.CASCADE)
    field_type = models.PositiveIntegerField('Field data type')
    lower_bound = models.PositiveIntegerField('Lower bound of random value', null=True)
    upper_bound = models.PositiveIntegerField('Upper bound of random value', null=True)
    sentence_count = models.PositiveIntegerField('Amount of sentences', null=True)


