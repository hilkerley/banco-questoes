# Generated by Django 2.1.2 on 2018-10-21 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questao',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='imagem da questão'),
        ),
    ]
