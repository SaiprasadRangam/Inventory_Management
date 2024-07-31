# Generated by Django 3.1.13 on 2023-07-06 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Name')),
                ('quantity', models.IntegerField(default=1)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
