# Generated by Django 2.1.5 on 2019-04-01 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('person', models.CharField(max_length=50)),
                ('attention', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='MyUser',
        ),
    ]