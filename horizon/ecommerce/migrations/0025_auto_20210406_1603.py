# Generated by Django 2.1 on 2021-04-06 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0024_auto_20210405_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='cidade',
            field=models.CharField(default='Sao Paulo', max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientes',
            name='estado',
            field=models.CharField(default='Sao Paulo', max_length=55),
            preserve_default=False,
        ),
    ]
