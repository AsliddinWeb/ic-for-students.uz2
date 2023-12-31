# Generated by Django 4.2.7 on 2023-11-30 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=455)),
            ],
        ),
        migrations.CreateModel(
            name='LogoSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='logos')),
            ],
        ),
        migrations.CreateModel(
            name='OneHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.CharField(default='#', max_length=255)),
                ('is_submenu', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneEmailSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone1', models.CharField(max_length=255)),
                ('phone2', models.CharField(max_length=255)),
                ('email1', models.CharField(max_length=255)),
                ('email2', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RightButtonSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SeoSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('keywords', models.TextField()),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=255)),
                ('favicon', models.FileField(upload_to='favicons')),
            ],
        ),
        migrations.CreateModel(
            name='SocialSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TelegramBotSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=455)),
                ('user_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TwoHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.CharField(default='#', max_length=255)),
                ('is_submenu', models.BooleanField(default=True)),
                ('one_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings_app.oneheader')),
            ],
        ),
    ]
