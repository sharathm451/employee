# Generated by Django 3.0.6 on 2020-06-20 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_id', models.IntegerField()),
                ('Emp_name', models.CharField(max_length=30)),
                ('Emp_salary', models.IntegerField()),
            ],
            options={
                'db_table': 'Emp',
            },
        ),
    ]