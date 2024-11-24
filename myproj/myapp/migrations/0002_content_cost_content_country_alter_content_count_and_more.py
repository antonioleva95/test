# Generated by Django 5.1.3 on 2024-11-16 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='cost',
            field=models.IntegerField(default=10, verbose_name='цена'),
        ),
        migrations.AddField(
            model_name='content',
            name='country',
            field=models.CharField(default='ru', max_length=20, verbose_name='страна'),
        ),
        migrations.AlterField(
            model_name='content',
            name='count',
            field=models.IntegerField(verbose_name='количество'),
        ),
        migrations.AlterField(
            model_name='content',
            name='description',
            field=models.CharField(max_length=300, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='content',
            name='dod',
            field=models.DateField(auto_now=True, verbose_name='дфта создания'),
        ),
        migrations.AlterField(
            model_name='content',
            name='name',
            field=models.CharField(max_length=25, verbose_name='наименование'),
        ),
    ]