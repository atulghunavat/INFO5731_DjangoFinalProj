# Generated by Django 3.0.5 on 2020-04-24 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('Paper_ID', models.IntegerField(help_text='Paper ID:', max_length=20, primary_key=True, serialize=False)),
                ('Paper_Title', models.CharField(help_text='Paper Title:', max_length=50)),
                ('Paper_Description', models.CharField(help_text='Paper Description:', max_length=280)),
                ('Project_ID', models.ForeignKey(db_column='Project_ID', on_delete=django.db.models.deletion.CASCADE, to='polls.Project')),
            ],
        ),
    ]