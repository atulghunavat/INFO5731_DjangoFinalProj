# Generated by Django 3.0.5 on 2020-05-03 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0004_auto_20200501_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papers',
            name='Paper_Content',
            field=models.FileField(default=0, help_text='Paper Content', upload_to=''),
        ),
    ]
