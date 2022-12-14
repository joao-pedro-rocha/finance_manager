# Generated by Django 4.1 on 2022-09-12 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_wallet_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extramoney',
            options={'verbose_name': 'Dinheiro extra', 'verbose_name_plural': 'Dinheiro extra'},
        ),
        migrations.AddField(
            model_name='expense',
            name='wallet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.wallet', verbose_name='Carteira'),
        ),
    ]
