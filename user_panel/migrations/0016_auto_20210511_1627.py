# Generated by Django 3.2 on 2021-05-11 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0015_alter_cartitem_sub_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]