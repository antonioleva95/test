# Generated by Django 5.1.3 on 2024-11-16 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_content_cost_content_country_alter_content_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='cost',
            field=models.IntegerField(default=0, verbose_name='цена'),
        ),
    ]
