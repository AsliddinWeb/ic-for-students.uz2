# Generated by Django 4.2.7 on 2023-12-22 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutme',
            options={'ordering': ['id'], 'verbose_name_plural': 'Men haqimda'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Tizimga kelgan xabarlar'},
        ),
    ]
