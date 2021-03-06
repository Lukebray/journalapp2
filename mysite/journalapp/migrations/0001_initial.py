# Generated by Django 3.0.7 on 2020-06-21 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_name', models.CharField(max_length=254)),
                ('created_date', models.DateTimeField(verbose_name='date published')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journalapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('content', models.TextField(max_length=10000)),
                ('created_date', models.DateTimeField(verbose_name='date published')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journalapp.Journal')),
            ],
        ),
    ]
