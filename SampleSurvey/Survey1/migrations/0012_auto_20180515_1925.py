# Generated by Django 2.0.4 on 2018-05-15 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Survey1', '0011_auto_20180515_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question1',
            name='A',
            field=models.BooleanField(default=False),
        ),
    ]
