# Generated by Django 4.1.1 on 2022-09-28 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sudo_chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='room',
            new_name='room_name',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='user',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='name',
            new_name='room_name',
        ),
    ]
