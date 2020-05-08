# Generated by Django 3.0.5 on 2020-04-30 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Papers',
            fields=[
                ('Paper_ID', models.IntegerField(help_text='Paper ID:', primary_key=True, serialize=False)),
                ('Paper_Title', models.CharField(help_text='Paper Title:', max_length=50)),
                ('Paper_Description', models.CharField(help_text='Paper Description:', max_length=280)),
                ('Paper_Content', models.FileField(default=0, help_text='Paper Content', upload_to='')),
                ('Project_ID', models.ForeignKey(db_column='Project_ID', default='', on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
            ],
            options={
                'db_table': 'Papers',
            },
        ),
    ]