# Generated by Django 2.0.5 on 2018-06-25 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAdmin', '0003_tuser_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuser',
            name='logintime',
            field=models.DateTimeField(blank=True, db_column='LoginTime', null=True),
        ),
    ]