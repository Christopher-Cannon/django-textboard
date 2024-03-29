# Generated by Django 2.2.3 on 2019-07-30 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=120)),
                ('locked', models.BooleanField(default=False)),
                ('pinned', models.BooleanField(default=False)),
                ('archived', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=False, default='Anonymous')),
                ('content', models.TextField()),
                ('hidden', models.BooleanField(default=False)),
                ('post_time', models.DateTimeField(auto_now=True)),
                ('thread', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='board.Thread')),
            ],
        ),
    ]
