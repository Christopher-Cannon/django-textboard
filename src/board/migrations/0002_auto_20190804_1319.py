# Generated by Django 2.2.3 on 2019-08-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hex_id',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='ip',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(default='Anonymous', max_length=64),
        ),
    ]
