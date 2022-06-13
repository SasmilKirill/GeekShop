

from django.db import migrations, models


class Migrations(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_lenght=128, unique=True, verbose_name='Название')),
                ('discription', models.TextField(verbose_name='ID')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категория',
                'ordering': ('name',),
            },
        ),
    ]
