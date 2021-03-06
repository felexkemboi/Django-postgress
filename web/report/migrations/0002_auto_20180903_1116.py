# Generated by Django 2.0 on 2018-09-03 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('oldprice', models.CharField(max_length=255)),
                ('newprice', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='post',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='board',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='starter',
        ),
        migrations.DeleteModel(
            name='Board',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
