# Generated by Django 3.2 on 2021-05-09 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0008_auto_20210509_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
