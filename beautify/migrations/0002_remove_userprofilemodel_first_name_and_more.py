# Generated by Django 4.2.7 on 2024-04-20 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautify', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofilemodel',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofilemodel',
            name='last_name',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='name',
            field=models.CharField(default='user', max_length=50),
            preserve_default=False,
        ),
    ]
