# Generated by Django 3.0.6 on 2020-05-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menucreator', '0002_menucategory_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menucategory',
            name='max_quantity',
            field=models.IntegerField(null=True),
        ),
    ]