# Generated by Django 4.2.7 on 2023-12-22 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_homemavjudyonalishlar_cap_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ['id'], 'verbose_name_plural': '10. Tizimga fayl yuklash'},
        ),
        migrations.AlterModelOptions(
            name='homeaboutme',
            options={'ordering': ['id'], 'verbose_name_plural': '5. Men haqimda'},
        ),
        migrations.AlterModelOptions(
            name='homeapp',
            options={'ordering': ['id'], 'verbose_name_plural': '8. Mobil ilova'},
        ),
        migrations.AlterModelOptions(
            name='homemavjudyonalishlar',
            options={'ordering': ['id'], 'verbose_name_plural': "4. Mavjud yo'nalishlar"},
        ),
        migrations.AlterModelOptions(
            name='homemehnatfaoliyatidivs',
            options={'ordering': ['id'], 'verbose_name_plural': "7. Mehnat faoliyatim | O'ng tomon"},
        ),
        migrations.AlterModelOptions(
            name='homemehnatfaoliyatim',
            options={'ordering': ['id'], 'verbose_name_plural': '6. Mehnat faoliyatim | Chap tomon'},
        ),
        migrations.AlterModelOptions(
            name='homequestion',
            options={'ordering': ['id'], 'verbose_name_plural': '9. Savollar bormi?'},
        ),
        migrations.AlterModelOptions(
            name='hometelegramgroup',
            options={'ordering': ['id'], 'verbose_name_plural': '9. Telegram guruh'},
        ),
        migrations.AlterModelOptions(
            name='homewelcome',
            options={'ordering': ['id'], 'verbose_name_plural': '1. Kirish oynasi'},
        ),
        migrations.AlterModelOptions(
            name='homeyonalishlar',
            options={'ordering': ['id'], 'verbose_name_plural': "2. Yo'nalishlar | Chap tomon"},
        ),
        migrations.AlterModelOptions(
            name='homeyonalishlardivs',
            options={'ordering': ['id'], 'verbose_name_plural': "3. Yo'nalishlar | O'ng tomon"},
        ),
    ]