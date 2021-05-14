# Generated by Django 3.2.2 on 2021-05-14 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Schema name')),
                ('separator', models.CharField(max_length=1, verbose_name='Field data separator sign')),
                ('string_character', models.CharField(max_length=1, verbose_name='String character')),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Column name')),
                ('field_type', models.PositiveIntegerField(verbose_name='Field data type')),
                ('lower_bound', models.PositiveIntegerField(null=True, verbose_name='Lower bound of random value')),
                ('upper_bound', models.PositiveIntegerField(null=True, verbose_name='Upper bound of random value')),
                ('sentence_count', models.PositiveIntegerField(null=True, verbose_name='Amount of sentences')),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generator.schema', verbose_name='Schema')),
            ],
        ),
    ]
