# Generated by Django 4.2.7 on 2024-07-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautify', '0002_remove_shopuser_email_remove_shopuser_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopprofilemodel',
            name='activity',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='shopprofilemodel',
            name='category',
        ),
        migrations.AddField(
            model_name='shopprofilemodel',
            name='category',
            field=models.ManyToManyField(to='beautify.categorymodel'),
        ),
    ]
