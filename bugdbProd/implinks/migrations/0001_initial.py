# Generated by Django 2.0.6 on 2018-06-14 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='implinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=30)),
                ('DESCR', models.CharField(max_length=240)),
                ('LINK', models.CharField(max_length=240)),
            ],
            options={
                'db_table': 'implinks',
            },
        ),
    ]
