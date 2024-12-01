# Generated by Django 5.0.6 on 2024-11-29 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='word_tr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_fr', models.CharField(max_length=50, verbose_name='متن در غالب الفبا')),
                ('word_lt', models.CharField(max_length=50, verbose_name='متن در نوشتار لاتین')),
                ('meaning', models.CharField(max_length=50, verbose_name='معنی در یک کلمه')),
                ('info', models.CharField(blank=True, max_length=50, null=True, verbose_name='توضیحات')),
            ],
        ),
    ]
