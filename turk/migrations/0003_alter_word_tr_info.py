# Generated by Django 5.0.6 on 2024-12-01 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turk', '0002_rename_word_fr_word_tr_word_pr_alter_word_tr_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word_tr',
            name='info',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='توضیحات به پارسی'),
        ),
    ]
