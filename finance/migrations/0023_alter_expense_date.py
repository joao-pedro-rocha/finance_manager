# Generated by Django 4.1 on 2023-03-08 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0022_alter_expense_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(null=True, verbose_name='Data'),
        ),
    ]
