# Generated by Django 2.1.5 on 2019-04-01 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190401_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='one',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='upload',
            name='thr',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='upload',
            name='two',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='upload',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
