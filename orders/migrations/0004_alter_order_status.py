# Generated by Django 3.2.18 on 2023-02-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('CREATED', 'Создан'), ('PAID', 'Оплачен'), ('ON_WAY', 'В пути'), ('DELIVERED', 'Доставлен')], default='CREATED', max_length=22),
        ),
    ]
