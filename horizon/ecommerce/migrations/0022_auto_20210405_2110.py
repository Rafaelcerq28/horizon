# Generated by Django 2.1 on 2021-04-06 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0021_carrinho_cor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='imagem',
            field=models.ImageField(default='images/fone_verde_f1rJ98E.jpg', upload_to='images/'),
            preserve_default=False,
        ),
    ]
